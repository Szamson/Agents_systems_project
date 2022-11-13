from mesa import *
from BattleModel.Weapon import *
from BattleModel.Armor import *
from BattleModel.Mount import *
import random


def random_weapon_melee():
    return random.choice([Sword, Dagger, Longsword, Mace, WarHammer, Spear])


def random_weapon_ranged():
    return random.choice([Bow, Longbow, Crossbow])


def random_armor():
    return random.choice([LeatherArmor, ChainMailArmor, PlateArmor])


def random_mount():
    return random.choice([Elephant, Horse])


class AgentModel(Agent):

    def __init__(self, unique_id, model, pos):
        super().__init__(unique_id=unique_id, model=model)

        self.unique_id = unique_id
        self.model = model
        self.pos = pos  # Position of the agent
        self.mount = None  # Type of mount the warrior is gonna ride
        self.weapon = None  # Type of weapon
        self.armor = None  # Type of armor
        self.bleeding_level = None  # How fast the agent is losing blood
        self.blood_left = None  # l on 60% fatal, 0.03 per level of bleeding per step
        self.pain_level = None  # In how much pain the agent is 0-100

    def step(self):
        pass


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

    def step(self):
        pass
