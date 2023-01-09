import numpy as np
from mesa.space import ContinuousSpace
from mesa.time import RandomActivation
from BattleModel.AgentModel import *


def contains(poly, x, y):
    """Determine whether a point lies inside a shape/polygon or not."""

    N = poly.points
    isInside = False

    for i in range(len(N)):
        v1 = N[i - 1]
        v2 = N[i]

        if (v2[1] > y) != (v1[1] > y):
            if x < (v1[0] - v2[0]) * (y - v2[1]) / (v1[1] - v2[1]) + v2[0]:
                isInside = not isInside

    return isInside


def calculate_red(model):
    return len([x for x in model.schedule.agents if x.army == "Red"])


def calculate_blue(model):
    return len([x for x in model.schedule.agents if x.army == "Blue"])


def battle_continious(model):
    red_number = calculate_red(model)
    blue_number = calculate_blue(model)

    if blue_number == 0 or red_number == 0:
        return False
    return True


def reporter(model):
    if calculate_red(model) > calculate_blue(model):
        return "Red"
    else:
        return "Blue"


class BattlefieldModel(Model):

    def __init__(self, width, height, n):
        super().__init__()
        self.test_n = n
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
        self.datacollector = DataCollector(
            model_reporters={"Army count - Red": calculate_red,
                             "Army count - Blue": calculate_blue, "winner": reporter})
        self.obstacle_list = [x for x in self.schedule.agents if x.__class__ == Obstacle]
        self.add_obstacles_to_dummy_board()

    def step(self):
        self.running = battle_continious(self)
        self.schedule.step()
        self.datacollector.collect(self)

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


        # squized rectangle

        # army_rows_1 = [5]
        #
        #
        # for row in army_rows_1:
        #     for comlumn in range(1, 99, 99):
        #         pos = np.array((comlumn, row))
        #         knight_b = Cavalry(
        #             row*1000+comlumn,
        #             self,
        #             pos,
        #             "Blue"
        #         )
        #         self.space.place_agent(knight_b, pos)
        #         self.schedule.add(knight_b)
        #
        # army_rows_3 = [5, 7, 9, 11, 13]
        #
        # for row in army_rows_3:
        #     for comlumn in range(1, 30, 5):
        #         pos = np.array((comlumn, row))
        #         knight_b = Infantry(
        #             row*1000+comlumn,
        #             self,
        #             pos,
        #             "Blue"
        #         )
        #         self.space.place_agent(knight_b, pos)
        #         self.schedule.add(knight_b)
        #
        #     for comlumn in range(65, 99, 6):
        #         pos = np.array((comlumn, row))
        #         knight_b = Infantry(
        #             row*1000+comlumn,
        #             self,
        #             pos,
        #             "Blue"
        #         )
        #         self.space.place_agent(knight_b, pos)
        #         self.schedule.add(knight_b)

        # army_rows_2 = [95]
        #
        # for row in army_rows_2:
        #     for comlumn in range(1, 99, self.test_n):
        #         pos = np.array((comlumn, row))
        #         knight_b = Infantry(
        #             row*1000+comlumn,
        #             self,
        #             pos,
        #             "Red"
        #         )
        #         self.space.place_agent(knight_b, pos)
        #         self.schedule.add(knight_b)


        # 7 and 8

        army_rows_1 = [5, 10, 15]
        army_rows_2 = [95, 90, 85]

        for row in army_rows_1:
            for comlumn in range(1, 99, 4):
                if row == army_rows_1[0]:
                    pos = np.array((comlumn, row))
                    knight_b = Ranger(
                        row+comlumn,
                        self,
                        pos,
                        "Blue"
                    )
                    self.space.place_agent(knight_b, pos)
                    self.schedule.add(knight_b)
                if row == army_rows_1[1]:
                    pos = np.array((comlumn, row))
                    knight_b = Infantry(
                        row+comlumn+99,
                        self,
                        pos,
                        "Blue"
                    )
                    self.space.place_agent(knight_b, pos)
                    self.schedule.add(knight_b)
                if row == army_rows_1[2]:
                    pos = np.array((comlumn, row))
                    knight_b = Cavalry(
                        row+comlumn+99*2,
                        self,
                        pos,
                        "Blue"
                    )
                    self.space.place_agent(knight_b, pos)
                    self.schedule.add(knight_b)

        for row in army_rows_2:
            for comlumn in range(1, 99, self.test_n):
                if row == army_rows_2[0]:
                    pos = np.array((comlumn, row))
                    knight_b = Ranger(
                        row+comlumn+99*67,
                        self,
                        pos,
                        "Red"
                    )
                    self.space.place_agent(knight_b, pos)
                    self.schedule.add(knight_b)
                if row == army_rows_2[1]:
                    pos = np.array((comlumn, row))
                    knight_b = Infantry(
                        row+comlumn+99*77,
                        self,
                        pos,
                        "Red"
                    )
                    self.space.place_agent(knight_b, pos)
                    self.schedule.add(knight_b)
                if row == army_rows_2[2]:
                    pos = np.array((comlumn, row))
                    knight_b = Cavalry(
                        row+comlumn+99*87,
                        self,
                        pos,
                        "Red"
                    )
                    self.space.place_agent(knight_b, pos)
                    self.schedule.add(knight_b)

        # Chaos test

        # for i in range(100):
        #     x = self.random.random() * self.space.x_max
        #     y = self.random.random() * self.space.y_max
        #     pos = np.array((x, y))
        #     unit = np.random.choice([1, 2, 3])
        #     if unit == 1:
        #
        #     elif unit == 2:
        #
        #     elif unit == 3:
        #         knight = Ranger(
        #             i,
        #             self,
        #             pos
        #         )
        #     self.space.place_agent(knight, pos)
        #     self.schedule.add(knight)

        # a = Obstacle(105, self, [[200.0, 200.0], [200.0, 300.0], [300.0, 300.0], [300.0, 200.0]])
        # self.space.place_agent(a, (50, 50))
        # self.schedule.add(a)
