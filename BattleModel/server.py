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


canvas = SimpleCanvas(draw, 500, 500)
model_params = {
    "width": 100,
    "height": 100
}

server = mesa.visualization.ModularServer(
    BattlefieldModel, [canvas], "Battle", model_params
)
