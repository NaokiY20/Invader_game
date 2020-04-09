import config
import random



Invaders = []    # reocrding all the invader instances

class AirCraft:
    def __init__(self, input_side=config.INVADER, inputel=config.MED):
        self.side = input_side
        self.level = inputel
        if self.side == config.FIGHTER:
            self.headpoint = [int(config.SCR_SIZ[config.HRZ]/2), config.SCR_SIZ[config.VRT] - config.SQR_SIZ * 2 - config.PAD_SIZ]
        elif self.side == config.INVADER:
            self.headpoint = [random.randint(config.PAD_SIZ + config.SQR_SIZ, config.SCR_SIZ[config.HRZ] - config.PAD_SIZ - config.SQR_SIZ), config.PAD_SIZ + config.SQR_SIZ]
        else:
            config.logging.error('UNEXPECTED VALUE of VALUE in AirCraft')
            config.sys.exit()


Fighter = AirCraft(config.FIGHTER)
