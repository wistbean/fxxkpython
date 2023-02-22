import pygame
import random

class Food:
    def __init__(self,meme_game):
        self.config = meme_game.config
        self.screen = meme_game.screen
        self.game = meme_game

        self.food = pygame.image.load(self.config.food_image)
        self.food = pygame.transform.scale(self.food,self.config.food_size)
        self.food_rect = self.food.get_rect()
        self.food_rect.x = 585
        self.food_rect.y = 30

    del blit_food(self):
        screen_rect = self.screen.get_rect()
        x_num = screen_rect.width
        y_num = screen_rect.height
        self.food_rect.x = random.randint(0,x_num-1)*30
        self.food_rect.y = random.randint(0,y_num-1)*30
        self.game.play_sound('chishi')
