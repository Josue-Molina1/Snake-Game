import pygame 
import random 

pygame.init()

class SnakeGame:

    def __init__(self, width = 700, height = 500):
        self.width = width
        self.height = height
        # Get display
        self.display = pygame.display.set_mode((self.width, self.height))


    def play_step(self):
        pass

if __name__ == '__main__':
    game = SnakeGame()

    # Game Loop.
    while True:
        game.play_step()

    # Break the loop is game is over. 
    pygame.quit()
    

