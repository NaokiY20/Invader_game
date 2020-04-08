#! /usr/bin/env python3
# IO.py

import pygame
from pygame.locals import *
import sys

import config



def aircraft_display(head_point, screen, side=config.INVADER):
    if side == config.INVADER:
        # head
        pygame.draw.rect(screen, config.INV_COL, Rect(head_point[0] - int(config.AIR_SQ_SIZ / 2), head_point[1] - int(config.AIR_SQ_SIZ / 2), config.AIR_SQ_SIZ, config.AIR_SQ_SIZ))
        # body
        pygame.draw.rect(screen, config.INV_COL, Rect(head_point[0] - int(config.AIR_SQ_SIZ / 2 * 3), head_point[1] - int(config.AIR_SQ_SIZ / 2 * 3), config.AIR_SQ_SIZ * 3, config.AIR_SQ_SIZ))
    elif side == config.FIGHTER:
        # head
        pygame.draw.rect(screen, config.FGT_COL, Rect(head_point[0] - int(config.AIR_SQ_SIZ / 2), head_point[1] - int(config.AIR_SQ_SIZ / 2), config.AIR_SQ_SIZ, config.AIR_SQ_SIZ))
        # body
        pygame.draw.rect(screen, config.FGT_COL, Rect(head_point[0] - int(config.AIR_SQ_SIZ / 2 * 3), head_point[1] + int(config.AIR_SQ_SIZ / 2), config.AIR_SQ_SIZ * 3, config.AIR_SQ_SIZ))
        

def main():
    # building the screen
    pygame.init()
    screen = pygame.display.set_mode(config.SCR_SIZ)
    pygame.display.set_caption("Test")

    while True:
        # back ground
        screen.fill(config.BCG_COL)

        # air crafts
        aircraft_display((30, 30), screen)
        aircraft_display((50, 70), screen, config.FIGHTER)
        
        
        pygame.display.update()

        # events
        for event in pygame.event.get():
            if event.type == QUIT:  # close button
                pygame.quit()
                sys.exit()

if __name__ == '__main__':
    main()
