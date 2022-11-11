from mesa import *



class AgentModel(Agent):

    def __init__(self, unique_id, model):
        super().__init__(unique_id=unique_id, model=model)

        self.unique_id = unique_id
        self.model = model
        self.pos = None

    def step(self):
        pass
