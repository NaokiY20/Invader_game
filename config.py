#! /usr/bin/env python3
# config.py

import logging
import sys

logging.basicConfig(level=logging.DEBUG,format='%(levelname)s - %(filename)s - L%(lineno)d - %(message)s')


# SIDES
INVADER = 1
FIGHTER = -1


# LEVELS
BGN = 1 # bginner
EAS = 2 # easy
MED = 3 # medium
HRD = 4 # hard
EXP = 5 # expert


# FOR DISPLAY INDEX
HRZ = 0 # horizontal
VRT = 1 # vertical


# DISPLAYED SIZE
SCR_SIZ = (400, 500)  # whole screen
PAD_SIZ = 10    # padding
SQR_SIZ = 8 # aircrafts are build four squares of siz * siz



# COLOURS (RGB max 255)
BCG_COL = (0, 0, 0)  # background (black)
FGT_COL = (0, 200, 0)  # fighter
INV_COL = (200, 0, 0)  # invaders
BUL_COL = (200, 200, 200)  # bullet (white)


# MOTION DISPLAY
# speed of aircrafts (classified by the level)
FGT_SPEED = 1   # fighter's
BGN_SPEED = 2
EAS_SPEED = 3
MED_SPEED = 4
HRD_SPEED = 5
EXP_SPEED = 6
