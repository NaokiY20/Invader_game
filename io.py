#! /usr/bin/env python3
# IO.py

import pygame
from pygame.locals import *

from config import *
import invader



def aircraft_display(head_point: list, screen, side=INVADER):
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
        

def bullet_display(tip_point: list, screen, side=INVADER):
    if side == FIGHTER:
        pygame.draw.line(screen, BUL_COL, tip_point, (tip_point[HRZ], tip_point[VRT] + BUL_SIZ))
    elif side == INVADER:
        pygame.draw.line(screen, BUL_COL, tip_point, (tip_point[HRZ], tip_point[VRT] - BUL_SIZ))
    else:
        logging.error('UNEXPECTED VALUE of SIDE in bullet_display')
        sys.exit()


def guard_display(screen):
    for sector in range(GRD_SCTR):
        for hrz in range(GRD_BLCS):
            for vrt in range(GRD_BLCS):
                if invader.Bullets[sector][hrz][vrt] == BLC_LEFT:
                    pygame.draw.rect(screen, BLC_COL, Rect(PAD_SIZ + SID_MRGN + sector * (BLC_SIZ * GRD_BLCS + GRD_INTV) + BLC_SIZ * hrz, SCR_SIZ[VRT] - PAD_SIZ - FGT_AREA - (GRD_BLCS - vrt) * BLC_SIZ, BLC_SIZ, BLC_SIZ))
                    

def main():
    # building the screen
    pygame.init()
    screen = pygame.display.set_mode(SCR_SIZ)
    pygame.display.set_caption("Test")
    fire_wait = 0
    
    while True:
        pressed_key = pygame.key.get_pressed()
        fire_wait = (fire_wait + 1) % BUL_WAIT
        
        
        ### KEY EVENTS
        # firing bullets
        if pressed_key[K_SPACE] and fire_wait == 0:
            bul = invader.Bullet(invader.Fighter.headpoint, FIGHTER)
            invader.Bullets.append(bul)
            bul.tip_place[VRT] += BUL_SIZ
        # moving the fighter
        if pressed_key[K_LEFT] and invader.Fighter.headpoint[HRZ] > PAD_SIZ + SQR_SIZ * 2:
            invader.Fighter.headpoint[HRZ] -= FGT_SPEED
        if pressed_key[K_RIGHT] and invader.Fighter.headpoint[HRZ] < SCR_SIZ[HRZ] - PAD_SIZ - SQR_SIZ * 2:
            invader.Fighter.headpoint[HRZ] += FGT_SPEED
        
        
        ### PARAMETERS CONTROL
        # proceeding bullets
        for bul in invader.Bullets:
            if bul.side == FIGHTER:
                bul.tip_place[VRT] -= BUL_SPEED
                # reaching the edge
                if bul.tip_place[VRT] >= SCR_SIZ[VRT] - PAD_SIZ:
                    invader.Bullets.remove(bul)
                    continue    # going on the outer loop
                # hitting an aircraft
                for inv in invader.Invaders:
                    if inv.headpoint[HRZ] - int(SQR_SIZ * 3 / 2) < bul.tip_place[HRZ] < inv.headpoint[HRZ] + int(SQR_SIZ * 3 / 2) and inv.headpoint[VRT] - int(SQR_SIZ * 3 / 2) <= bul.tip_place[VRT] < inv.headpoint[VRT] + int(SQR_SIZ / 2) - BUL_SIZ:
                        invader.Bullets.remove(bul)
                        inv.life -= 1
                        break
                else:
                    continue    # going on the inner loop
                continue    # going on the outer loop
            elif bul.side == INVADER:
                bul.tip_place[VRT] += BUL_SPEED
                # reaching the edge
                if bul.tip_place[VRT] <= PAD_SIZ:
                    invader.Bullets.remove(bul)
                    continue    # going on the outer loop
                # hitting the fighter
                elif invader.Fighter.headpoint[HRZ] - int(SQR_SIZ * 3 / 2) < bul.tip_place[HRZ] < invader.Fighter.headpoint[HRZ] + int(SQR_SIZ * 3 / 2) and invader.Fighter.headpoint[VRT] - int(SQR_SIZ / 2) <= bul.tip_place[VRT] < invader.Fighter.headpoint[VRT] + int(SQR_SIZ * 3 / 2) + BUL_SIZ:
                    invader.Bullets.remove(bul)
                    invader.Fighter.life -= 1
                 
                
        ### DISPLAY
        # background
        screen.fill(BCG_COL)

        # aircrafts
        for inv in invader.Invaders:
            aircraft_display(inv.headpoint, screen)
        aircraft_display(invader.Fighter.headpoint, screen, FIGHTER)

        # bullets
        for bul in invader.Bullets:
            bullet_display(bul.tip_place, screen)

        # guards
        guard_display(screen)
   

        ### SPECIAL EVENTS
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
                

        ### SCREEN UPLOAD
        pygame.display.update()

        ### LOADING TIME
        pygame.time.wait(100)






if __name__ == '__main__':
    for ref in range(3):
        inv = invader.AirCraft()
        invader.Invaders.append(inv)

        
    main()
