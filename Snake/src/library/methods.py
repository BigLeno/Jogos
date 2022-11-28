import pygame, random
from pygame.locals import *

class Snake_Game ():
    def __init__(self):
        """Game builder function"""
        self.UP = 0
        self.RIGHT = 1
        self.DOWN = 2
        self.LEFT = 3
        self.points = 0
        self.condition = False
        self.my_direction = 3 #Starts to the left
        self.screen = 0 #Starts in menu screen

    def get_test (self):
        """Apenas para testar"""
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((600, 600))
        pygame.display.set_caption('Cobrinha')
        self.font = pygame.font.Font('freesansbold.ttf', 18)

        return self.clock, self.screen, self.font, self.condition

    def on_grid_random (self):
        """Function that randomizes the appearance of the fruit"""
        x = random.randint(0,59)
        y = random.randint(0,59)
        self.apple_pos = (x * 10, y * 10)

        return self.apple_pos

    def get_snake(self):
        """Function that makes the snake"""
        self.snake = [(200, 200), (210, 200), (220,200)]
        #self.snake_skin = pygame.Surface((10,10))
        #self.snake_skin.fill((255,255,255)) #Setting the color of the snake (White)         
        return self.snake
    
    def get_snake_skin(self):
        self.snake_skin = pygame.Surface((10, 10))
        self.snake_skin.fill((255,255,255))

        for pos in self.snake:
            self.screen.blit(self.snake_skin, pos)

        return self.snake_skin


    def get_apple(self):
        """Function that makes the apple"""
        self.apple = pygame.Surface((10,10))
        self.apple_pos = self.on_grid_random()
        self.apple.fill((255, 0, 0)) #Setting the color of the snake (Red)
        self.screen.blit(self.apple, self.apple_pos)

    def collision (self, c1, c2):
        """Function that establishes the collision"""
        self.collision_condition = (c1[0] == c2[0]) and (c1[1] == c2[1])
        return self.collision_condition

    def earn_points (self):
        """Function that makes the snake earn points""" 
        if self.collision(self.snake, self.apple_pos) == True:
            self.points += 1

        return self.points

    def grow_snake (self):
        """Function that makes the snakes grow"""
        if self.collision(self.snake[0], self.apple_pos) == True:
            self.snake.append((0,0))

    def edge_collision (self):
        """Function that establishes the collision at the edges"""
        if self.snake[0][0] == 600 or self.snake[0][1] == 600 or self.snake[0][0] < 0 or self.snake[0][1] < 0:
            self.condition = True
            return self.condition

    def auto_collision (self):
        """Function that establishes the collision of the snake with itself"""
        for i in range(1, len(self.snake) - 1):
            if self.snake[0][0] == self.snake[i][0] and self.snake[0][1] == self.snake[i][1]:
                self.condition = True
                break

    def get_movement (self):
        """Function that estabilishes the movement of the snake"""
        for i in range(len(self.snake) - 1, 0, -1):
            self.snake[i] = (self.snake[i-1][0], self.snake[i-1][1])

    def get_movement_direction (self):
        """Function that establishes the movement direction of the snake"""
        match self.my_direction:
            case self.UP:
                self.snake[0] = (self.snake[0][0], self.snake[0][1] - 10)
            case self.DOWN:
                self.snake[0] = (self.snake[0][0], self.snake[0][1] + 10)
            case self.RIGHT:
                self.snake[0] = (self.snake[0][0] + 10, self.snake[0][1])
            case self.LEFT:
                self.snake[0] = (self.snake[0][0] - 10, self.snake[0][1])
            case _:
                pass
        

    def get_movement_events (self, event):
        """Function that captures movement events"""
        if event.type == KEYDOWN:
            if event.key == K_UP and self.my_direction != self.DOWN:
                self.my_direction = self.UP
            elif event.key == K_DOWN and self.my_direction != self.UP:
                self.my_direction = self.DOWN
            elif event.key == K_LEFT and self.my_direction != self.RIGHT:
                self.my_direction = self.LEFT
            elif event.key == K_RIGHT and self.my_direction != self.LEFT:
                self.my_direction = self.RIGHT
            else:
                pass

    def get_screen_events (self, event):
        """Function that captures screen events"""
        if event.type == QUIT:
            pygame.quit()
            exit()
            
        elif event.type == KEYDOWN:
            if event.key == K_ESCAPE and self.screen == 2:
                self.screen = 3 #Pause screen
            else:
                pass


