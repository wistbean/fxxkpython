# -*- coding:utf-8 -*-
import pygame
import random


class InitGameData:
    snake_init_pos = [[250,250], [240,250], [230,250], [220,250]] #蛇的初始位置
    head_pos = [250, 250]
    white_color = (255, 255, 255) #白色rgb
    black_color = (0, 0, 0)
    cell = 10

    def __init__(self, width, heigh):
        self.width = width
        self.heigh = heigh

    def hit_the_self(self):
        if self.snake_init_pos[0] in self.snake_init_pos[1:]:
            return True
        else:
            return False

    def hit_the_wall(self, head_pos):
        if head_pos[0] >= self.width or head_pos[0] < 0 or head_pos[1] >= self.heigh or head_pos[1] < 0:
            return True
        else:
            return False

class myPygameConfig(InitGameData):

    def setTitle(self, game_title):
        pygame.display.set_caption(game_title)  #设置标题

    def initPygame(self):
        pygame.init()

    def initClock(self):
        clock = pygame.time.Clock()
        return clock

    def getCaption(self):
        caption = pygame.display.set_mode((self.width, self.heigh)) #画布，注意 双括号
        return caption


class setCaption(InitGameData):
    food__pos = [random.randrange(1, 50) * 10, random.randrange(1, 50) * 10]

    def __init__(self, width, heigh, caption):
        super().__init__(width, heigh)
        self.caption = caption

    def draw_rect(self, color, position):
        pygame.draw.rect(self.caption, color, pygame.Rect(position[0], position[1], super().cell, super().cell)) #绘制矩阵

    def setBackGround(self):
        self.caption.fill(super().black_color)

    def init_food_pos(self):
        self.food__pos = [random.randrange(1, 50) * 10, random.randrange(1, 50) * 10] #食物初始随机位置

    def change_direction(self, head_pos):

        super().snake_init_pos.insert(0, list(head_pos)) #吃到食物，新增一格，更新蛇头的位置，列表开头插入新位置

        if head_pos != self.food__pos:
            super().snake_init_pos.pop() #若没有吃到食物，移除蛇尾，也就是列表最后一个元素
        else:
            self.init_food_pos()

        if super().hit_the_self() or super().hit_the_wall(head_pos):
            #死
            pygame.quit()

        print(super().snake_init_pos)

def main():
   capWidth = 500
   capHeigh = 500
   myinitdata = InitGameData(capWidth, capHeigh)

   myPygame = myPygameConfig(capWidth, capHeigh)
   myPygame.setTitle("EatSnake")
   myPygame.initPygame()
   caption = myPygame.getCaption()
   mySetCap = setCaption(capWidth, capHeigh, caption)

   for pos in myinitdata.snake_init_pos:
        mySetCap.draw_rect(myinitdata.white_color, pos)

   mySetCap.draw_rect(myinitdata.white_color, mySetCap.food__pos)
   pygame.display.update()

   while 1:
       for event in pygame.event.get():
           if event.type == pygame.QUIT:
               pygame.quit()

           if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                   print("左")
                   myinitdata.head_pos[0] -= myinitdata.cell
                   mySetCap.change_direction(myinitdata.head_pos)
                elif event.key == pygame.K_RIGHT:
                   print("右")
                   myinitdata.head_pos[0] += myinitdata.cell
                   mySetCap.change_direction(myinitdata.head_pos)
                elif event.key == pygame.K_UP:
                   print("上")
                   myinitdata.head_pos[1] -= myinitdata.cell
                   mySetCap.change_direction(myinitdata.head_pos)
                elif event.key == pygame.K_DOWN:
                   print("下")
                   myinitdata.head_pos[1] += myinitdata.cell
                   mySetCap.change_direction(myinitdata.head_pos)

       mySetCap.setBackGround()
       mySetCap.draw_rect(myinitdata.white_color, mySetCap.food__pos)
       for pos in myinitdata.snake_init_pos:
            mySetCap.draw_rect(myinitdata.white_color, pos)

       pygame.display.update()

       myPygame.initClock().tick(10)

if __name__ == '__main__':
    main()


