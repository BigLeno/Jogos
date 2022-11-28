
import pygame, random
from pygame.locals import *

# função que define aonde a maça vai aparecer
def on_grid_random():
    x = random.randint(0,59)
    y = random.randint(0,59)
    return (x * 10, y * 10)

#função para a colisão
def collision(c1, c2):
    return (c1[0] == c2[0]) and (c1[1] == c2[1])

# Definindo o movimento.
UP = 0
RIGHT = 1
DOWN = 2
LEFT = 3

pygame.init()
screen = pygame.display.set_mode((600, 600))
pygame.display.set_caption('Cobrinha')

cobra = [(200, 200), (210, 200), (220,200)]
cobra_skin = pygame.Surface((10,10))
cobra_skin.fill((255,255,255)) #cor da cobrinha branca

maça_pos = on_grid_random()
maça = pygame.Surface((10,10))
maça.fill((255,0,0))

my_direction = LEFT

clock = pygame.time.Clock()

font = pygame.font.Font('freesansbold.ttf', 18)
pontos = 0

perdeu = False
while not perdeu:
    clock.tick(10)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()

        if event.type == KEYDOWN:
            if event.key == K_UP and my_direction != DOWN:
                my_direction = UP
            if event.key == K_DOWN and my_direction != UP:
                my_direction = DOWN
            if event.key == K_LEFT and my_direction != RIGHT:
                my_direction = LEFT
            if event.key == K_RIGHT and my_direction != LEFT:
                my_direction = RIGHT

    
    ## função caso coma a maça cobra cresça e ganhe um ponto
    if collision(cobra[0], maça_pos):
        maça_pos = on_grid_random()
        cobra.append((0,0))
        pontos = pontos + 1
        
    # função caso bater na borda perder
    if cobra[0][0] == 600 or cobra[0][1] == 600 or cobra[0][0] < 0 or cobra[0][1] < 0:
        perdeu = True
        break
    
    # função de para caso bater em si mesmo perder
    for i in range(1, len(cobra) - 1):
        if cobra[0][0] == cobra[i][0] and cobra[0][1] == cobra[i][1]:
            perdeu = True
            break

    if perdeu:
        break
    
    for i in range(len(cobra) - 1, 0, -1):
        cobra[i] = (cobra[i-1][0], cobra[i-1][1])
        
    # função que faz a cobra realmente se mover 
    if my_direction == UP:
        cobra[0] = (cobra[0][0], cobra[0][1] - 10)
    if my_direction == DOWN:
        cobra[0] = (cobra[0][0], cobra[0][1] + 10)
    if my_direction == RIGHT:
        cobra[0] = (cobra[0][0] + 10, cobra[0][1])
    if my_direction == LEFT:
        cobra[0] = (cobra[0][0] - 10, cobra[0][1])
    
    screen.fill((0,0,0))
    screen.blit(maça, maça_pos)
    
    for x in range(0, 600, 10): ## faz as linhas laterais
        pygame.draw.line(screen, (40, 40, 40), (x, 0), (x, 600))
    for y in range(0, 600, 10): # faz as linhas verticais
        pygame.draw.line(screen, (40, 40, 40), (0, y), (600, y))
    
    pontos_font = font.render('Pontuação: %s' % (pontos), True, (255, 255, 255))
    pontos_rect = pontos_font.get_rect()
    pontos_rect.topleft = (600 - 120, 10)
    screen.blit(pontos_font, pontos_rect)
    
    for pos in cobra:
        screen.blit(cobra_skin,pos)

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
