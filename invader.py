import config


class AirCraft:
    def __init__(self, input_side=config.INVADER, input_level=config.MED_LEV):
        self.side = input_side
        self.level = input_level
        