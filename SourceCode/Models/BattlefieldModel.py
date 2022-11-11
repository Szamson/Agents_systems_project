from mesa import *
from mesa.space import ContinuousSpace
from mesa.time import RandomActivation


class BattlefieldModel(Model):

    def __init__(self, width, height):
        super().__init__()

        self.width = width
        self.height = height
        self.grid = ContinuousSpace(
            x_max=self.width,
            y_max=self.height,
            torus=False)
        self.schedule = RandomActivation(self)


    def step(self):
        pass
