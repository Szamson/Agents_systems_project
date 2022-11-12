from enum import Enum


class WeaponType(Enum):
    RANGED = 1
    BLADES = 2
    BLUNT = 3
    POLEARM = 4


class Injuries(Enum):
    CUT = 1
    STAB = 2
    CRUSH = 3
    BRUISE = 4


class Weapon:

    def __init__(self):
        self.type_of_injury_inflicted = None
        self.attack_speed = None  # how many steps till next attack
        self.type = None
        self.range = None  # m


class Sword(Weapon):

    def __init__(self):
        super().__init__()
        self.type_of_injury_inflicted = [Injuries.CUT, Injuries.STAB]
        self.attack_speed = 1
        self.type = WeaponType.BLADES
        self.range = 0.9


class Dagger(Weapon):

    def __init__(self):
        super().__init__()
        self.type_of_injury_inflicted = [Injuries.CUT, Injuries.STAB]
        self.attack_speed = 1
        self.type = WeaponType.BLADES
        self.range = 0.25


class Longsword(Weapon):

    def __init__(self):
        super().__init__()
        self.type_of_injury_inflicted = [Injuries.CUT, Injuries.STAB]
        self.attack_speed = 1
        self.type = WeaponType.BLADES
        self.range = 1.3


class Mace(Weapon):

    def __init__(self):
        super().__init__()
        self.type_of_injury_inflicted = [Injuries.BRUISE, Injuries.CRUSH]
        self.attack_speed = 1
        self.type = WeaponType.BLUNT
        self.range = 0.7


class WarHammer(Weapon):

    def __init__(self):
        super().__init__()
        self.type_of_injury_inflicted = [Injuries.BRUISE, Injuries.CRUSH]
        self.attack_speed = 1
        self.type = WeaponType.BLUNT
        self.range = 1.65


class Spear(Weapon):

    def __init__(self):
        super().__init__()
        self.type_of_injury_inflicted = [Injuries.STAB]
        self.attack_speed = 1
        self.type = WeaponType.POLEARM
        self.range = 2.5


class Bow(Weapon):

    def __init__(self):
        super().__init__()
        self.type_of_injury_inflicted = [Injuries.STAB]
        self.attack_speed = 2
        self.type = WeaponType.RANGED
        self.range = 27


class Longbow(Weapon):

    def __init__(self):
        super().__init__()
        self.type_of_injury_inflicted = [Injuries.STAB]
        self.attack_speed = 2
        self.type = WeaponType.RANGED
        self.range = 45


class Crossbow(Weapon):

    def __init__(self):
        super().__init__()
        self.type_of_injury_inflicted = [Injuries.STAB]
        self.attack_speed = 3
        self.type = WeaponType.RANGED
        self.range = 55
