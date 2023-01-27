# -*- coding:utf-8 -*-
import pygame
import random

caption_width=500#画布宽度
caption_height=500#画布高度
white_color=(255,255,255)#设置颜色
black_color=(0,0,0)
game_title='贪吃蛇'
cell=10#格子，10像素点
food_pos=[random.randrange(1,50)*10,random.randrange(1,50)*10]#食物随机位置

class game:
    def __init__(self):
        self.snake_init_pos=[[250,250],[240,250],[230,250],[220,250]]#蛇初始位置
        self.head_pos = [250,250]#蛇头位置

    def hit_the_wall(self):
        if self.head_pos[0]>=caption_width or self.head_pos[0]<0 or self.head_pos[1]>=caption_height or self.head_pos[1]<0:
            return True
        else:
            return False

    def hit_it_self(self):
        if self.snake_init_pos[0] in self.snake_init_pos[1:]:
            return True
        else:
            return False

    def change_direction(self):
        global food_pos
        self.snake_init_pos.insert(0, list(self.head_pos))  # 在列表中第一位添加新蛇头位置

        # 头的位置与食物位置不等则删除列表最后一个元素，表示蛇的移动。否则不删除即吃到食物，加的那一格不用删除。
        if self.head_pos != food_pos:  # !=：不等于。
            self.snake_init_pos.pop()  # 删除列表中最后一个元素
        else:
            food_pos=[random.randrange(1,50)*10,random.randrange(1,50)*10]

        if self.hit_it_self() or self.hit_the_wall():
            pygame.quit()

def main():
    pygame.init()
    clock=pygame.time.Clock()
    pygame.display.set_caption(game_title)  # 设置游戏名称
    caption = pygame.display.set_mode((caption_width, caption_height))  # 设置窗口大小

    def draw_rect(color, position):  # 定义通用位置函数
        pygame.draw.rect(caption, color, pygame.Rect(position[0], position[1], cell, cell))

    snaker=game()
    for pos in snaker.snake_init_pos:
        draw_rect(white_color,pos)
    draw_rect(white_color,food_pos)

    pygame.display.update()

    while 1:#方向监听
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_LEFT:
                    snaker.head_pos[0]-=cell
                    snaker.change_direction()
                elif event.key==pygame.K_RIGHT:
                    snaker.head_pos[0] += cell
                    snaker.change_direction()
                elif event.key==pygame.K_UP:
                    snaker.head_pos[1] -= cell
                    snaker.change_direction()
                elif event.key==pygame.K_DOWN:
                    snaker.head_pos[1] += cell
                    snaker.change_direction()

        caption.fill(black_color)#每更新一次需要渲染一下画布
        for pos in snaker.snake_init_pos:
            draw_rect(white_color,pos)
        draw_rect(white_color, food_pos)

        pygame.display.update()
        clock.tick(10)

if __name__=='__main__':
    main()






