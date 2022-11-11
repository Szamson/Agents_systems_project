class Mount:

    def __init__(self):
        self.max_speed = None
        self.health = None
        self.chance_to_flee = None


class Elephant(Mount):

    def __init__(self):
        super().__init__()
        self.max_speed = 40  # km/h
        self.health = 5221  # kg
        self.chance_to_flee = 0.5  # scared easily


class Horse(Mount):

    def __init__(self):
        super().__init__()
        self.max_speed = 88  # km/h
        self.health = 300  # kg
        self.chance_to_flee = 0.1  # hardly scared
