from mesa import *
from mesa.space import ContinuousSpace
from mesa.time import RandomActivation
from SourceCode.Models.AgentModel import *


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
        self.fill_battlefield_TEST()

    def step(self):
        self.schedule.step()



    def fill_battlefield_TEST(self):
        self.grid.place_agent(Infantry, (50, 50))
