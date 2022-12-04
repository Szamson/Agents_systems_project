import numpy as np
from mesa.space import ContinuousSpace
from mesa.time import RandomActivation
from BattleModel.AgentModel import *


def calculate_red(model):
    return len([x for x in model.schedule.agents if x.army == "Red"])


def calculate_blue(model):
    return len([x for x in model.schedule.agents if x.army == "Blue"])


class BattlefieldModel(Model):

    def __init__(self, width, height):
        super().__init__()

        self.width = width
        self.height = height
        self.space = ContinuousSpace(
            x_max=self.width,
            y_max=self.height,
            torus=False)
        self.schedule = RandomActivation(self)
        self.fill_battlefield_TEST()
        self.running = True
        self.data_collector = DataCollector(
            model_reporters={"Army count - Red": calculate_red,
                             "Army count - Blue": calculate_blue})

    def step(self):
        self.schedule.step()
        self.data_collector.collect(self)

    def fill_battlefield_TEST(self):
        for i in range(100):
            x = self.random.random() * self.space.x_max
            y = self.random.random() * self.space.y_max
            pos = np.array((x, y))
            unit = np.random.choice([1, 2, 3])
            if unit == 1:
                knight = Infantry(
                    i,
                    self,
                    pos
                )
            elif unit == 2:
                knight = Cavalry(
                    i,
                    self,
                    pos
                )
            elif unit == 3:
                knight = Ranger(
                    i,
                    self,
                    pos
                )
            self.space.place_agent(knight, pos)
            self.schedule.add(knight)
