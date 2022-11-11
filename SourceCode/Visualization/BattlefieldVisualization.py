from mesa.visualization.modules import CanvasGrid
from mesa.visualization.ModularVisualization import ModularServer
from mesa.visualization.modules import ChartModule

from SourceCode.Models.BattlefieldModel import BattlefieldModel
import SourceCode.Models


def StartSimulation(field_size):
    grid = CanvasGrid(field_size, field_size, 500, 500)

    server = ModularServer(BattlefieldModel,
                           [grid],
                           "Draw Model",
                           {"width": field_size, "height": field_size})
    server.port = 8521  # The default
    server.launch()
