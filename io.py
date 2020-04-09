#! /usr/bin/env python3
# IO.py

import pygame
from pygame.locals import *

from config import *
import invader



def aircraft_display(head_point, screen, side=INVADER):
    if side == INVADER:
        # head
        pygame.draw.rect(screen, INV_COL, Rect(head_point[0] - int(SQR_SIZ / 2), head_point[1] - int(SQR_SIZ / 2), SQR_SIZ, SQR_SIZ))
        # body
        pygame.draw.rect(screen, INV_COL, Rect(head_point[0] - int(SQR_SIZ / 2 * 3), head_point[1] - int(SQR_SIZ / 2 * 3), SQR_SIZ * 3, SQR_SIZ))
    elif side == FIGHTER:
        # head
        pygame.draw.rect(screen, FGT_COL, Rect(head_point[0] - int(SQR_SIZ / 2), head_point[1] - int(SQR_SIZ / 2), SQR_SIZ, SQR_SIZ))
        # body
        pygame.draw.rect(screen, FGT_COL, Rect(head_point[0] - int(SQR_SIZ / 2 * 3), head_point[1] + int(SQR_SIZ / 2), SQR_SIZ * 3, SQR_SIZ))
        

def bullet_display(tip_point, screen):
    pygame.draw.line(screen, BUL_COL, tip_point, (tip_point[HRZ], tip_point[VRT] + BUL_SIZ))
    


def main():
    # building the screen
    pygame.init()
    screen = pygame.display.set_mode(SCR_SIZ)
    pygame.display.set_caption("Test")
    bullet_wait = 0
    
    while True:
        pressed_key = pygame.key.get_pressed()
        bullet_wait = (bullet_wait + 1) % BUL_WAIT
        
        # firing bullets
        if pressed_key[K_SPACE] and bullet_wait == 0:
            bul = invader.Bullet(invader.Fighter.headpoint, FIGHTER)
            invader.Bullets.append(bul)
        # moving the fighter
        if pressed_key[K_UP] and invader.Fighter.headpoint[VRT] > PAD_SIZ + SQR_SIZ * 2:
            invader.Fighter.headpoint[VRT] -= FGT_SPEED
        if pressed_key[K_DOWN] and invader.Fighter.headpoint[VRT] < SCR_SIZ[VRT] - PAD_SIZ - SQR_SIZ * 2:
            invader.Fighter.headpoint[VRT] += FGT_SPEED
        if pressed_key[K_LEFT] and invader.Fighter.headpoint[HRZ] > PAD_SIZ + SQR_SIZ * 2:
            invader.Fighter.headpoint[HRZ] -= FGT_SPEED
        if pressed_key[K_RIGHT] and invader.Fighter.headpoint[HRZ] < SCR_SIZ[HRZ] - PAD_SIZ - SQR_SIZ * 2:
            invader.Fighter.headpoint[HRZ] += FGT_SPEED
        # proceeding bullets
        for bul in invader.Bullets:
            bul.tip_place[VRT] -= BUL_SPEED
            # reaching the other side
            if bul.tip_place[VRT] <= PAD_SIZ:
                invader.Bullets.remove(bul)


        # BACK GROUND
        screen.fill(BCG_COL)


        # AIRCRAFTS DISPLAY
        for inv in invader.Invaders:
            aircraft_display(inv.headpoint, screen)
        aircraft_display(invader.Fighter.headpoint, screen, FIGHTER)

        # BULLETS DISPLAY
        for bul in invader.Bullets:
            bullet_display(bul.tip_place, screen)
                    

        # EVENTS
        for event in pygame.event.get():
            # close button
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            # another key
            if event.type == KEYDOWN:
                # quit the game
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                

        # screen upload
        pygame.display.update()

        # loading time
        pygame.time.wait(5)






if __name__ == '__main__':
    for ref in range(3):
        inv = invader.AirCraft()
        invader.Invaders.append(inv)

        
    main()
