from BattleModel.server import server
from mesa.batchrunner import FixedBatchRunner, batch_run
from BattleModel.BattlefieldModel import BattlefieldModel
import pandas as pd

if __name__ == '__main__':
    # parameters = {"width": 100, "height": 100}
    #
    # a = batch_run(BattlefieldModel, parameters=parameters, iterations=10000, max_steps=100)
    #
    # b = pd.DataFrame.from_dict(a)
    # win_inf = len([a for a in b["winner"] == "Cavalry" if a == True])
    # win_cav = len([a for a in b["winner"] == "Ranger" if a == True])
    # draw = len([a for a in b["winner"] == "Draw" if a == True])
    # print(f"Cavalry wins :  {win_inf}")
    # print(f"Ranger wins :  {win_cav}")
    # print(f"Draws :  {draw}")

    # print([a for a in b["winner"] == "Infantry" if True])
    #
    # print(b)

    server.launch()
