import numpy as np
from mesa.space import ContinuousSpace
from mesa.time import RandomActivation
from BattleModel.AgentModel import *



class BattlefieldModel(Model):

    def __init__(self, width, height):
        super().__init__()

        self.width = width
        self.height = height
        self.space = ContinuousSpace(
            x_max=self.width,
            y_max=self.height,
            torus=True)
        self.schedule = RandomActivation(self)
        self.fill_battlefield_TEST()
        self.running = True


    def step(self):
        self.schedule.step()



    def fill_battlefield_TEST(self):
        for i in range(100):
            x = self.random.random() * self.space.x_max
            y = self.random.random() * self.space.y_max
            pos = np.array((x, y))
            knight = Infantry(
                i,
                self,
                pos
            )
            self.space.place_agent(knight, pos)
            self.schedule.add(knight)
