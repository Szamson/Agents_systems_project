from enum import Enum


class WeaponType(Enum):
    RANGED = 1
    BLADES = 2
    BLUNT = 3
    POLEARM = 4


class Weapon:

    def __init__(self):
        self.damage = None  # TODO THINK ALBOUT ALL OF THEM
        self.attack_speed = None
        self.type = None
        self.range = None  # m


class Sword(Weapon):

    def __init__(self):
        super().__init__()
        self.damage = None
        self.attack_speed = None
        self.type = WeaponType.BLADES
        self.range = 0.9


class Dagger(Weapon):

    def __init__(self):
        super().__init__()
        self.damage = None
        self.attack_speed = None
        self.type = WeaponType.BLADES
        self.range = 0.25


class Longsword(Weapon):

    def __init__(self):
        super().__init__()
        self.damage = None
        self.attack_speed = None
        self.type = WeaponType.BLADES
        self.range = 1.3


class Mace(Weapon):

    def __init__(self):
        super().__init__()
        self.damage = None
        self.attack_speed = None
        self.type = WeaponType.BLUNT
        self.range = 0.7


class WarHammer(Weapon):

    def __init__(self):
        super().__init__()
        self.damage = None
        self.attack_speed = None
        self.type = WeaponType.BLUNT
        self.range = 1.65


class Spear(Weapon):

    def __init__(self):
        super().__init__()
        self.damage = None
        self.attack_speed = None
        self.type = WeaponType.POLEARM
        self.range = 2.5


class Bow(Weapon):

    def __init__(self):
        super().__init__()
        self.damage = None
        self.attack_speed = None
        self.type = WeaponType.RANGED
        self.range = 27


class Longbow(Weapon):

    def __init__(self):
        super().__init__()
        self.damage = None
        self.attack_speed = None
        self.type = WeaponType.RANGED
        self.range = 45


class Crossbow(Weapon):

    def __init__(self):
        super().__init__()
        self.damage = None
        self.attack_speed = None
        self.type = WeaponType.RANGED
        self.range = 55
