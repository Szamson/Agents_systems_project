class Mount:

    def __init__(self):
        self.max_speed = None  # km/h
        self.pain_level = None  # 0 - 100
        self.chance_to_flee = None  # scared modifier


class Elephant(Mount):

    def __init__(self):
        super().__init__()
        self.max_speed = 40
        self.pain_level = 0
        self.chance_to_flee = 0.5


class Horse(Mount):

    def __init__(self):
        super().__init__()
        self.max_speed = 88
        self.pain_level = 0
        self.chance_to_flee = 0.1
