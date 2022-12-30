import numpy as np
from mesa.space import ContinuousSpace
from mesa.time import RandomActivation
from BattleModel.AgentModel import *


def contains(poly, x, y):
    """Determine whether a point lies inside a shape/polygon or not."""

    N = poly.points
    isInside = False

    for i in range(len(N)):
        v1 = N[i-1]
        v2 = N[i]

        if (v2[1] > y) != (v1[1] > y):
            if x < (v1[0] - v2[0]) * (y - v2[1]) / (v1[1] - v2[1]) + v2[0]:
                isInside = not isInside

    return isInside


def calculate_red(model):
    return len([x for x in model.schedule.agents if x.army == "Red"])


def calculate_blue(model):
    return len([x for x in model.schedule.agents if x.army == "Blue"])


class BattlefieldModel(Model):

    def __init__(self, width, height):
        super().__init__()

        self.x_max = 100
        self.y_max = 100
        self.width = width
        self.height = height
        self.dummy_board = np.ones((self.x_max, self.y_max))
        self.space = ContinuousSpace(
            x_max=self.x_max,
            y_max=self.y_max,
            torus=False)
        self.schedule = RandomActivation(self)
        self.fill_battlefield_TEST()
        self.running = True
        self.data_collector = DataCollector(
            model_reporters={"Army count - Red": calculate_red,
                             "Army count - Blue": calculate_blue})
        self.obstacle_list = [x for x in self.schedule.agents if x.__class__ == Obstacle]
        self.add_obstacles_to_dummy_board()

    def step(self):
        self.schedule.step()
        self.data_collector.collect(self)

    def add_obstacles_to_dummy_board(self):

        for i in range(len(self.dummy_board)):
            for j in range(len(self.dummy_board[0])):
                if self.is_in_obstacles((j, i)):
                    self.dummy_board[i][j] = 0



    def is_in_obstacles(self, pos):
        for obs in self.obstacle_list:
            if contains(obs, pos[0], pos[1]):
                return True
        return False


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

        a = Obstacle(105, self, [[50.0, 50.0], [50.0, 70.0], [70.0, 70.0], [70.0, 50.0]])
        self.space.place_agent(a, (50, 50))
        self.schedule.add(a)
