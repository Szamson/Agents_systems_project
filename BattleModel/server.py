import mesa

from BattleModel.BattlefieldModel import BattlefieldModel
from BattleModel.SimpleCanvas import SimpleCanvas
from BattleModel.AgentModel import *


def draw(agent):
    if agent.__class__ == Infantry:
        return {"Shape": "circle", "r": 2, "Filled": "true", "Color": agent.army}
    if agent.__class__ == Cavalry:
        return {"Shape": "triangle", "a": 4, "Filled": "true", "Color": agent.army}
    if agent.__class__ == Ranger:
        return {"Shape": "rect", "w": 0.01, "h": 0.01, "Filled": "true", "Color": agent.army}
    if agent.__class__ == Obstacle:
        return {"Shape": "polygon", "list_of_points": agent.points, "Filled": "true", "Color": "Black"}


chart = mesa.visualization.ChartModule([
    {"Label": "Army count - Red", "Color": "Red"},
    {"Label": "Army count - Blue", "Color": "Blue"}],
    data_collector_name='datacollector')

canvas = SimpleCanvas(draw, 500, 500)
model_params = {
    "width": 100,
    "height": 100
}

server = mesa.visualization.ModularServer(
    BattlefieldModel, [canvas, chart], "Battle", model_params
)
