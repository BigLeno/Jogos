
import pygame, random
from pygame.locals import *

from library.methods import Snake_Game 

sg = Snake_Game()

pygame.init()

clock, screen, font, condition = sg.get_test()
snake = sg.get_snake()
apple = sg.get_apple()



while condition != True:
    clock.tick(10)
    for event in pygame.event.get():
        sg.get_movement_events(event)
        sg.get_screen_events(event)

    sg.on_grid_random()
    points = sg.earn_points()
    sg.grow_snake()
    sg.edge_collision()
    sg.auto_collision()
    sg.get_movement()
    
    
    screen.fill((0,0,0))
    
    for x in range(0, 600, 10): ## faz as linhas laterais
        pygame.draw.line(screen, (40, 40, 40), (x, 0), (x, 600))
    for y in range(0, 600, 10): # faz as linhas verticais
        pygame.draw.line(screen, (40, 40, 40), (0, y), (600, y))
    
    pontos_font = font.render('Pontuação: %s' % (points), True, (255, 255, 255))
    pontos_rect = pontos_font.get_rect()
    pontos_rect.topleft = (600 - 120, 10)
    screen.blit(pontos_font, pontos_rect)

    pygame.display.update()

 ## função aparecer game over na tela
while True:
    perdeu_font = pygame.font.Font('freesansbold.ttf', 75)
    perdeu_screen = perdeu_font.render('Perdeu', True, (255, 255, 255))
    perdeu_rect = perdeu_screen.get_rect()
    perdeu_rect.midtop = (600 / 2, 10)
    screen.blit(perdeu_screen, perdeu_rect)
    pygame.display.update()
    pygame.time.wait(500)
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit()
