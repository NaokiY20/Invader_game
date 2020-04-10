import config
import random


class AirCraft:
    def __init__(self, input_side=config.INVADER, input_level=config.MED):
        self.side = input_side
        if self.side == config.FIGHTER:
            self.headpoint = [int(config.SCR_SIZ[config.HRZ] / 2), config.SCR_SIZ[config.VRT] - config.PAD_SIZ - config.PAD_SIZ - config.SQR_SIZ * 2]
            self.level = config.FGT
            self.life = config.LIFE_MAX
        elif self.side == config.INVADER:
            self.headpoint = [random.randint(config.PAD_SIZ + config.SQR_SIZ, config.SCR_SIZ[config.HRZ] - config.PAD_SIZ - config.SQR_SIZ), config.PAD_SIZ + config.SQR_SIZ]
            self.level = input_level
            self.life = 1
        else:
            config.logging.error('UNEXPECTED VALUE of VALUE in AirCraft')
            config.sys.exit()


class Bullet:
    def __init__(self, headpoint: list, input_side=config.INVADER):
        self.side = input_side
        self.tip_place = [headpoint[0], headpoint[1]]


# INITIALIZATION
Invaders = [] # reocrding all the invader instances
Bullets = []  # recording all the bullet instances
Blocks = []
# fighter
Fighter = AirCraft(config.FIGHTER)
# blocks
for sector in range(config.GRD_SCTR):
    Blocks.append([])
    for hrz in range(config.GRD_BLCS):
        Blocks[sector].append([])
        for vrt in range(config.GRD_BLCS):
            Blocks[sector][hrz].append(config.BLC_LEFT)
