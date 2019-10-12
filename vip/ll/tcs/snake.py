# -*- coding:utf-8 -*-
import pygame
import random
class Tcs():
    def __init__(self):
        self.score=0
        self.fx="up"#初始方向
        self.caption_width = 500  #画布宽度
        self.caption_height = 500 #画布高度
        self.white_color = (255, 255, 255) # 白色rgb
        self.black_color = (0, 0, 0)
        self.game_title = '贪吃蛇'
        self.cell = 10 # 格子
        self.snake_init_pos = [[250,250], [240,250], [230,250], [220,250]] # 蛇的初始位置
        self.food_pos = [random.randrange(1, 50) * 10, random.randrange(1, 50) * 10] # 食物初始随机位置
        self.head_pos = [250, 250]#蛇头
        pygame.init() # 初始化 pygame
        self.clock = pygame.time.Clock()
        self.caption = pygame.display.set_mode((self.caption_width, self.caption_height))#画布设置
        pygame.display.set_caption(self.game_title)
    def draw_rect(self,color, position):#出生地
         pygame.draw.rect(self.caption, color, pygame.Rect(position[0], position[1], self.cell, self.cell))

    def hit_the_self(self):#是否首尾撞击
        if self.snake_init_pos[0] == self.snake_init_pos[-1]:
            return True
        else:
            return False

    def hit_the_wall(self,head_pos):#是否撞墙
        if head_pos[0] >=510 or head_pos[0]<-1 or head_pos[1] >= 510or head_pos[1] < -1:
            return True
        else:
            return False

    def change_direction(self):#移动

        self.snake_init_pos.insert(0, list(self.head_pos))
        if self.fx == 'left':
            self.head_pos[0] -= self.cell
        elif self.fx == 'right':
            self.head_pos[0] += self.cell
        elif self.fx == 'up':
            self.head_pos[1] -= self.cell
        elif self.fx == 'down':
            self.head_pos[1] += self.cell
        if self.head_pos != self.food_pos:
            self.snake_init_pos.pop()
        else:
            self.score+=1
            self.food_pos = [random.randrange(1, 50) * 10, random.randrange(1, 50) * 10]

        if  self.hit_the_self() or self.hit_the_wall(self.head_pos):#判断是否撞墙

            pygame.quit()

    def result(self):
        font = pygame.font.Font('./aa.ttf', 30)
        final_text2 = "Your  score is:  " + str(self.score)
        surface=font.render(final_text2,False,(250,100,100))
        self.caption.blit(surface,(100,100))
        pygame.display.flip()

    def main(self):
        for pos in self.snake_init_pos:
            self.draw_rect(self.white_color, pos)
        while 1:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT and self.fx!='right':
                        self.fx="left"
                    elif event.key == pygame.K_RIGHT and self.fx!='left':
                        self.fx ='right'
                    elif event.key == pygame.K_UP and self.fx!='down':
                        self.fx = 'up'
                    elif event.key == pygame.K_DOWN and self.fx!='up':
                        self.fx = 'down'
            self.change_direction()
            self.caption.fill(self.black_color)
            self.draw_rect(self.white_color, self.food_pos)
            for pos in self.snake_init_pos:
                self.draw_rect(self.white_color, pos)
            self.result()
            pygame.display.update()
            self.clock.tick(10)
if __name__ == '__main__':
    tc=Tcs()
    tc.main()









