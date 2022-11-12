import mesa

from SourceCode.Models.BattlefieldModel import BattlefieldModel
from SourceCode.Visualization.SimpleCanvas import SimpleCanvas


def draw():
    return {"Shape": "circle", "r": 2, "Filled": "true", "Color": "Red"}


canvas = SimpleCanvas(draw, 500, 500)
model_params = {
    "width": 100,
    "height": 100
}

server = mesa.visualization.ModularServer(
    BattlefieldModel, [canvas], "Boids", model_params
)
