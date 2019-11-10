# -*- coding:utf-8 -*-
import pygame
import random
import time


class InitGameData:
    snake_init_pos = [[250,250], [240,250], [230,250], [220,250]] #蛇的初始位置
    head_pos = [250, 250]
    white_color = (255, 255, 255) #白色rgb
    black_color = (0, 0, 0)
    red_color = (255, 0, 0)
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
        self.caption = pygame.display.set_mode((self.width, self.heigh)) #画布，注意 双括号
        return self.caption

    def initBackGroundMusic(self):
        pygame.mixer.music.load("music/background.wav")
        pygame.mixer.music.play(-1, 0.0)

    def initSnakeDieSound(self):
        dieSound = pygame.mixer.Sound("music/die.wav")
        return dieSound

    def initEatfoodSound(self):
        foodSound = pygame.mixer.Sound("music/eat.wav") #Sound不支持mp3
        return foodSound


    def initScoreFont(self):
        self.fontColor = pygame.Color(150, 150,150)
        self.mygameFont = pygame.font.SysFont('font/Arial.ttf', 26)


    def drawScore(self, score):
        # print('drawScore:{}'.format(score))
        scoreSurf = self.mygameFont.render('Score:%s'%(score), True, self.fontColor)
        scoreRect = scoreSurf.get_rect()
        scoreRect.midtop = (self.width-50, 10)
        self.caption.blit(scoreSurf, scoreRect)
        pygame.display.flip()

    # # 疑问：这个函数调用self.mygameOverFont总是报错
    # # AttributeError: 'setGameCaption' object has no attribute 'mygameFont'
    # def drawGameOver(self):
    #     print('GameOver')
    #     gameOverSurf = self.mygameFont.render('Game Over!', True, self.fontColor)
    #     gameOverRect = gameOverSurf.get_rect()
    #     gameOverRect.midtop = (250, 200)
    #     self.caption.blit(gameOverSurf, gameOverRect)
    #     pygame.display.flip()

    def drawGameOver(self):
        gameOverColor = pygame.Color(250,0, 0)
        mygameFont = pygame.font.SysFont('font/Arial.ttf', 60)
        gameOverSurf = mygameFont.render('Game Over!', True, gameOverColor)
        gameOverRect = gameOverSurf.get_rect()
        gameOverRect.midtop = (250, 200)
        self.caption.blit(gameOverSurf, gameOverRect)
        pygame.display.flip()

    def gameQuit(self):
        self.drawGameOver()
        pygame.mixer.music.stop()
        self.initSnakeDieSound().play()
        time.sleep(3) #为了听挂了时候音效，再关闭窗口
        pygame.quit()


class setGameCaption(myPygameConfig):
    food__pos = [random.randrange(1, 50) * 10, random.randrange(1, 50) * 10]
    score = 0

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
            super().initEatfoodSound().play() #吃到食物声效
            self.score += 1
            print('score:{}'.format(self.score))

        if super().hit_the_self() or super().hit_the_wall(head_pos):
            #死
            super().gameQuit()
        # print(super().snake_init_pos)

def main():
    capWidth = 500
    capHeigh = 500
    myinitdata = InitGameData(capWidth, capHeigh)

    myPygame = myPygameConfig(capWidth, capHeigh)
    myPygame.setTitle("EatSnake")
    myPygame.initPygame()
    caption = myPygame.getCaption()
    myPygame.initBackGroundMusic()
    myPygame.initScoreFont()
    mySetCap = setGameCaption(capWidth, capHeigh, caption)


    for pos in myinitdata.snake_init_pos:
        mySetCap.draw_rect(myinitdata.white_color, pos)

    mySetCap.draw_rect(myinitdata.red_color, mySetCap.food__pos)
    myPygame.drawScore(0)
    pygame.display.update()

    while 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
               pygame.quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    myinitdata.head_pos[0] -= myinitdata.cell
                    mySetCap.change_direction(myinitdata.head_pos)
                elif event.key == pygame.K_RIGHT:
                    myinitdata.head_pos[0] += myinitdata.cell
                    mySetCap.change_direction(myinitdata.head_pos)
                elif event.key == pygame.K_UP:
                    myinitdata.head_pos[1] -= myinitdata.cell
                    mySetCap.change_direction(myinitdata.head_pos)
                elif event.key == pygame.K_DOWN:
                    myinitdata.head_pos[1] += myinitdata.cell
                    mySetCap.change_direction(myinitdata.head_pos)

        mySetCap.setBackGround()
        mySetCap.draw_rect(myinitdata.red_color, mySetCap.food__pos)
        for pos in myinitdata.snake_init_pos:
            mySetCap.draw_rect(myinitdata.white_color, pos)

        myPygame.drawScore(mySetCap.score)
        pygame.display.update()

        myPygame.initClock().tick(10)

if __name__ == '__main__':
    main()


