import pygame, sys
from pygame.locals import QUIT

pygame.init()
venster = pygame.display.set_mode((1920, 1080))
venster.fill((255,255,255))
color = (0,0,0)
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if pygame.mouse.get_pressed() == (True,False,False):
            pygame.draw.circle(venster, color, pygame.mouse.get_pos(),50)
        if pygame.mouse.get_pressed() == (False, False, True):
                    pygame.draw.circle(venster, (255, 255, 255), pygame.mouse.get_pos(), 50)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                color = (255,42,0)
            if event.key == pygame.K_b:
                    color = (0, 0, 0)
            if event.key == pygame.K_g:
                color = (255, 255, 0)
            if event.key == pygame.K_y:
                color = (105,105,105)
            if event.key == pygame.K_s:
                pygame.image.save(venster, "tekening" + ".jpg")
    pygame.display.update()
