from mesa import *



class AgentModel(Agent):

    def __init__(self, unique_id, model):
        super().__init__(unique_id=unique_id, model=model)

        self.unique_id = unique_id
        self.model = model
        self.pos = None  # Position of the agent
        self.mount = None  # Type of mount the warrior is gonna ride
        self.weapon = None  # Type of weapon
        self.armor = None  # Type of armor
        self.bleeding_level = None  # How fast the agent is losing blood
        self.pain_level = None  # In how much pain the agent is

    def step(self):
        pass



