from mesa import *
from BattleModel.Weapon import *
from BattleModel.Armor import *
from BattleModel.Mount import *
from pathfinding.core.diagonal_movement import DiagonalMovement
from pathfinding.core.grid import Grid
from pathfinding.finder.a_star import AStarFinder
import random
import numpy as np
import math


def random_weapon_melee():
    return random.choice([Sword(), Dagger(), Longsword(), Mace(), WarHammer(), Spear()])


def random_weapon_ranged():
    return random.choice([Bow(), Longbow(), Crossbow()])


def random_armor():
    return random.choice([LeatherArmor(), ChainMailArmor(), PlateArmor()])


def random_mount():
    return random.choice([Elephant(), Horse()])


def random_army():
    return random.choice(["Blue", "Red"])


def intersect(p1, p2, p3, p4):
    """Returns a boolean. Check if 2 lines are intersecting."""

    uA = ((p4[0] - p3[0]) * (p1[1] - p3[1]) - (p4[1] - p3[1]) * (p1[0] - p3[0])) / (
                (p4[1] - p3[1]) * (p2[0] - p1[0]) - (p4[0] - p3[0]) * (p2[1] - p1[1]))
    uB = ((p2[0] - p1[0]) * (p1[1] - p3[1]) - (p2[1] - p1[1]) * (p1[0] - p3[0])) / (
                (p4[1] - p3[1]) * (p2[0] - p1[0]) - (p4[0] - p3[0]) * (p2[1] - p1[1]))

    if 0 <= uA <= 1 and 0 <= uB <= 1:
        return 1


class AgentModel(Agent):

    def __init__(self, unique_id, model, pos):
        super().__init__(unique_id=unique_id, model=model)

        self.original_blood_level = 5.67

        self.unique_id = unique_id
        self.model = model
        self.pos = pos  # Position of the agent
        self.mount = None  # Type of mount the warrior is gonna ride
        self.weapon = None  # Type of weapon
        self.armor = None  # Type of armor
        self.bleeding_level = None  # How fast the agent is losing blood
        self.blood_left = None  # l on 60% fatal, 0.03 per level of bleeding per step
        self.pain_level = None  # In how much pain the agent is 0-100
        self.army = None  # For who they are fighting
        self.vision = 80  # What the agent see

    def step(self):

        if not self.attack():
            self.move_to_closest_target()
        self.bleed()

    def calculate_hit(self, weapon):
        armor = self.armor.dmg_reduction
        is_hit = np.random.choice([True, False], 1, p=[1 - armor, armor])
        if is_hit:
            injury = random.choice(weapon.type_of_injury_inflicted)
            self.apply_wound(injury)

    def apply_wound(self, type_of_injury):
        if type_of_injury == Injuries.CUT:
            self.bleeding_level = self.bleeding_level + 2
        elif type_of_injury == Injuries.STAB:
            self.bleeding_level = self.bleeding_level + 1
        elif type_of_injury == Injuries.BRUISE:
            self.pain_level = self.pain_level + random.randint(1, 5)
        elif type_of_injury == Injuries.CRUSH:
            self.pain_level = self.pain_level + random.randint(6, 10)
        self.check_if_dead()

    def move_to_closest_target(self):

        blood_loss_slow = self.blood_left / self.original_blood_level
        pain_slow = 1 - self.pain_level / 100
        armor_slow = 1 - self.armor.weight / 100

        speed = 12 * blood_loss_slow * pain_slow * armor_slow

        nemesis = self.closest_enemy()

        if nemesis is None:
            return

        for obs in self.model.obstacle_list:
            for i in range(len(obs.points)):
                if intersect(self.pos, nemesis.pos, obs.points[i-1], obs.points[i]):
                    pathfinder = True
                    break
                else:
                    pathfinder = False

        if pathfinder:

            grid = Grid(matrix=self.model.dummy_board)

            start = grid.node(math.floor(self.pos[0]), math.floor(self.pos[1]))
            end = grid.node(math.floor(nemesis.pos[0]), math.floor(nemesis.pos[1]))

            finder = AStarFinder(diagonal_movement=DiagonalMovement.always)
            path, runs = finder.find_path(start, end, grid)

            if len(path) - 1 > speed:

                temp_new_pos = path[math.floor(speed)]
                new_x = self.pos[0] - math.floor(self.pos[0]) + temp_new_pos[0]
                new_y = self.pos[1] - math.floor(self.pos[1]) + temp_new_pos[1]
                new_pos = (new_x, new_y)
            else:
                temp_new_pos = path[-1]
                new_x = self.pos[0] - math.floor(self.pos[0]) + temp_new_pos[0]
                new_y = self.pos[1] - math.floor(self.pos[1]) + temp_new_pos[1]
                new_pos = (new_x, new_y)

            if 0 < new_pos[0] < float(self.model.width) and 0 < new_pos[1] < float(self.model.height):
                self.model.space.move_agent(self, new_pos)


        else:

            distance_to_nemesis = self.model.space.get_distance(self.pos, nemesis.pos)

            distance_needed = distance_to_nemesis - self.weapon.range

            my_x, my_y = self.pos
            op_x, op_y = nemesis.pos

            new_x = abs(my_x - op_x) - distance_needed + op_x
            new_y = abs(my_y - op_y) - distance_needed + op_y

            new_x_speed = abs(my_x - op_x) - speed + op_x
            new_y_speed = abs(my_y - op_y) - speed + op_y

            if speed > distance_needed:
                new_pos = (new_x, new_y)
            else:
                new_pos = (new_x_speed, new_y_speed)
            if 0 < new_pos[0] < float(self.model.width) and 0 < new_pos[1] < float(self.model.height):
                self.model.space.move_agent(self, new_pos)

    def scout(self):
        neighbors = self.model.space.get_neighbors(self.pos, self.vision, False)
        enemies = []
        for x in neighbors:
            if x.army == self.army or x.army is None:
                pass
            else:
                enemies.append(x)
        return enemies

    def closest_enemy(self):
        targets = self.scout()
        if len(targets) > 0:
            return min(targets, key=lambda value: self.model.space.get_distance(self.pos, value.pos))
        else:
            return None

    def attack(self):
        nemesis = self.closest_enemy()

        if nemesis is None:
            return False

        if self.model.space.get_distance(self.pos, nemesis.pos) < self.weapon.range:
            nemesis.apply_wound(np.random.choice(self.weapon.type_of_injury_inflicted))
        else:
            return False
        return True

    def bleed(self):
        self.blood_left -= self.bleeding_level * 0.03
        self.check_if_dead()

    def check_if_dead(self):

        if self.blood_left < self.blood_left * 0.6 or self.pain_level > 80:
            self.model.space.remove_agent(self)
            self.model.schedule.remove(self)


class Infantry(AgentModel):

    def __init__(self, unique_id, model, pos):
        super().__init__(unique_id=unique_id, model=model, pos=pos)

        self.unique_id = unique_id
        self.model = model
        self.pos = pos
        self.mount = None
        self.weapon = random_weapon_melee()
        self.armor = random_armor()
        self.bleeding_level = 0
        self.blood_left = 5.67
        self.pain_level = 0
        self.army = random_army()  # TODO change for smf that makes more sense


class Cavalry(AgentModel):
    def __init__(self, unique_id, model, pos):
        super().__init__(unique_id=unique_id, model=model, pos=pos)

        self.unique_id = unique_id
        self.model = model
        self.pos = pos
        self.mount = random_mount()
        self.weapon = random_weapon_melee()
        self.armor = random_armor()
        self.bleeding_level = 0
        self.blood_left = 5.67
        self.pain_level = 0
        self.army = random_army()


class Ranger(AgentModel):
    def __init__(self, unique_id, model, pos):
        super().__init__(unique_id=unique_id, model=model, pos=pos)

        self.unique_id = unique_id
        self.model = model
        self.pos = pos
        self.mount = None
        self.weapon = random_weapon_ranged()
        self.armor = random_armor()
        self.bleeding_level = 0
        self.blood_left = 5.67
        self.pain_level = 0
        self.army = random_army()


class Obstacle(Agent):

    def __init__(self, unique_id, model, points_position):
        super().__init__(unique_id=unique_id, model=model)

        self.original_blood_level = 5.67

        self.unique_id = unique_id
        self.model = model
        self.points = points_position  # points of polygon as [(x, y),(x, y), (x, y)]
        self.army = None

    def step(self) -> None:
        pass
