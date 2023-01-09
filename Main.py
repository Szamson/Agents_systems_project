from BattleModel.server import server
from mesa.batchrunner import FixedBatchRunner, batch_run
from BattleModel.BattlefieldModel import BattlefieldModel
import pandas as pd

if __name__ == '__main__':
    server.launch()
    # parameters = {"width": 100, "height": 100, "n": 99}
    #
    # a = batch_run(BattlefieldModel, parameters=parameters, iterations=10000, max_steps=500)
    #
    # b = pd.DataFrame.from_dict(a)
    # win_blue = len([a for a in b["winner"] == "Blue" if a == True])
    # win_red = len([a for a in b["winner"] == "Red" if a == True])
    # print(f"Blue wins :  {win_blue}")
    # print(f"Red wins :  {win_red}")
    # print(f"Draws :  {draw}")

    # print([a for a in b["winner"] == "Infantry" if True])
    #
    # print(b)
    #


