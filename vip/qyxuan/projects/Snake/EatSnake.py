import random
import pygame
from pygame.locals import *

caption_width = 500 #画布宽度
caption_heigh = 500 #画面高度
white_color = (255, 255, 255) #白色rgb
game_title = 'EatSnakeGame'
cell = 10 # 格子
snake_init_pos = [[250,250], [240,250], [230,250], [220,250]] #蛇的初始位置
food_pos = [random.randrange(1, 50) * 10, random.randrange(1, 50) * 10] #食物初始随机位置

pygame.init() #初始化 pygame

caption = pygame.display.set_mode((caption_width, caption_heigh))
pygame.display.set_caption(game_title)

def draw_rect(color, position):
    pygame.draw.rect(caption, color, pygame.Rect(position[0], position[1], cell, cell))


def main():
    for pos in snake_init_pos:
        draw_rect(white_color, pos)

    draw_rect(white_color, food_pos)
    pygame.display.update()

