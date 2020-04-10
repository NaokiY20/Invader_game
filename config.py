#! /usr/bin/env python3
# config.py

import logging
import sys

logging.basicConfig(level=logging.DEBUG,format='%(levelname)s - %(filename)s - L%(lineno)d - %(message)s')


### SIDES
INVADER = 1
FIGHTER = -1


### LEVELS
FGT = 0 # fighter
BGN = 1 # bginner
EAS = 2 # easy
MED = 3 # medium
HRD = 4 # hard
EXP = 5  # expert


### FIGHTER LIFE
LIFE_MAX = 1


### FOR DISPLAY INDEX
HRZ = 0 # horizontal
VRT = 1 # vertical


### DISPLAYED SIZE
SCR_SIZ = (400, 500)  # whole screen
PAD_SIZ = 10    # padding
SQR_SIZ = 8 # aircrafts are build four squares of siz * siz
BUL_SIZ = 5  # bullets
BLC_SIZ = 3  # blocks of a guard
FGT_AREA = (SQR_SIZ * 2) * 3    # the height of fighter's area


### COLOURS (RGB max 255)
BCG_COL = (0, 0, 0)  # background (black)
FGT_COL = (0, 200, 0)  # fighter
INV_COL = (200, 0, 0)  # invaders
BUL_COL = (255, 255, 255)  # bullet (white)
BLC_COL = (150, 150, 150)  # blocks


### MOTION DISPLAY
# speed of aircrafts (classified by the level)
FGT_SPEED = 1  # fighter's
BUL_SPEED = 3
BUL_WAIT = BUL_SIZ * 10  # interval during which next bullet is fired; as a bullet is long, this interval gets longer


### GUARDS
GRD_SCTR = 4  # the number of guard 
GRD_BLCS = 20  # each guard is composed of GRD_BLCS * GRD_BLCS square
BLC_LEFT = 1  # block is left
BLC_DSTR = 0  # block is destroyed (disappear)
SID_MRGN = SQR_SIZ * 6  # margins width of both side of guards
GRD_INTV = (SCR_SIZ[HRZ] - (PAD_SIZ * 2 + SID_MRGN * 2 + GRD_BLCS * BLC_SIZ * GRD_SCTR)) / (GRD_SCTR - 1)  # guard intetrval
"""
whole SCR_SIZ is filled as the follows
    PAD_SIZ SID_MRGN SQR_SIZ*GRD_BLCS GRD_INTV SQR_SIZ*GRD_BLCS GRD_INTV ... SQR_SIZ*GRD_BLCS SID_MRGN PAD_SIZ
"""
