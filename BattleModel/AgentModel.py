from mesa import *
from BattleModel.Weapon import *
from BattleModel.Armor import *
from BattleModel.Mount import *
import random
import numpy as np


def random_weapon_melee():
    return random.choice([Sword, Dagger, Longsword, Mace, WarHammer, Spear])


def random_weapon_ranged():
    return random.choice([Bow, Longbow, Crossbow])


def random_armor():
    return random.choice([LeatherArmor, ChainMailArmor, PlateArmor])


def random_mount():
    return random.choice([Elephant, Horse])


def random_army():
    return random.choice(["Blue", "Red"])


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
        self.army = None

    def step(self):
        pass

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

    def move(self):
        blood_loss_slow = self.blood_left / self.original_blood_level
        pain_slow = 1 - self.pain_level / 100
        armor_slow = 1 - self.armor.weight / 100

        speed = 12 * blood_loss_slow * pain_slow * armor_slow

        # TODO finish moving





class Infantry(AgentModel):

    def __init__(self, unique_id, model, pos):
        super().__init__(unique_id=unique_id, model=model, pos=pos)

        self.unique_id = unique_id
        self.model = model
        self.pos = pos
        self.mount = None
        self.weapon = random_weapon_melee()
        self.armor = random_armor()
        self.bleeding_level = None
        self.blood_left = 5.67
        self.pain_level = 0
        self.army = random_army()  # TODO change for smf that makes more sense

    def step(self):
        pass


class Cavalry(AgentModel):
    def __init__(self, unique_id, model, pos):
        super().__init__(unique_id=unique_id, model=model, pos=pos)

        self.unique_id = unique_id
        self.model = model
        self.pos = pos
        self.mount = random_mount()
        self.weapon = random_weapon_melee()
        self.armor = random_armor()
        self.bleeding_level = None
        self.blood_left = 5.67
        self.pain_level = 0
        self.army = random_army()

    def step(self):
        pass


class Ranger(AgentModel):
    def __init__(self, unique_id, model, pos):
        super().__init__(unique_id=unique_id, model=model, pos=pos)

        self.unique_id = unique_id
        self.model = model
        self.pos = pos
        self.mount = None
        self.weapon = random_weapon_ranged()
        self.armor = random_armor()
        self.bleeding_level = None
        self.blood_left = 5.67
        self.pain_level = 0
        self.army = random_army()

    def step(self):
        pass
