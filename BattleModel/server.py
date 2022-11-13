import mesa

from BattleModel.BattlefieldModel import BattlefieldModel
from BattleModel.SimpleCanvas import SimpleCanvas


def draw(agent):
    return {"Shape": "circle", "r": 2, "Filled": "true", "Color": "Red"}


canvas = SimpleCanvas(draw, 500, 500)
model_params = {
    "width": 100,
    "height": 100
}

server = mesa.visualization.ModularServer(
    BattlefieldModel, [canvas], "Battle", model_params
)
