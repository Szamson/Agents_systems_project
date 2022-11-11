class Armor:

    def __init__(self):
        #  self.weakness = None TODO when all works
        self.dmg_reduction = None
        self.weight = None  # kg --> calculate speed reduction based on knight weight


class PlateArmor(Armor):

    def __init__(self):
        super().__init__()
        #  self.weakness = None
        self.dmg_reduction = 0.5
        self.weight = 27


class LeatherArmor(Armor):

    def __init__(self):
        super().__init__()
        #  self.weakness = None
        self.dmg_reduction = 0.1
        self.weight = 4  # TODO Fact check it


class ChainMailArmor(Armor):

    def __init__(self):
        super().__init__()
        #  self.weakness = None
        self.dmg_reduction = 0.3
        self.weight = 10  # TODO Fact check it
