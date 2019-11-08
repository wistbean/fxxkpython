# -*- coding:utf-8 -*-
import random
import pygame


caption_width = 500 #画布宽度
caption_heigh = 500 #画面高度
white_color = (255, 255, 255) #白色rgb
black_color = (0, 0, 0)
game_title = 'EatSnakeGame'
cell = 10 # 格子的宽高

head_pos = [250, 250]

pygame.init() #初始化 pygame
clock = pygame.time.Clock()

caption = pygame.display.set_mode((caption_width, caption_heigh)) #画布
pygame.display.set_caption(game_title)  #设置标题

def draw_rect(color, position):
    pygame.draw.rect(caption, color, pygame.Rect(position[0], position[1], cell, cell)) #绘制矩阵


snake_init_pos = [[250,250], [240,250], [230,250], [220,250]] #蛇的初始位置
food_pos = [random.randrange(1, 50) * 10, random.randrange(1, 50) * 10] #食物初始随机位置
def change_direction(head_pos):
    #都在代码开头定义过
    # 为什么snake_init_pos在这里可以不用全局
    global food_pos
    snake_init_pos.insert(0, list(head_pos)) #吃到食物，新增一格，更新蛇头的位置，列表开头插入新位置

    if head_pos != food_pos:
        snake_init_pos.pop() #若没有吃到食物，移除蛇尾，也就是列表最后一个元素
    else:
        food_pos = [random.randrange(1, 50) * 10, random.randrange(1, 50) * 10]

    if hit_the_self() or hit_the_wall(head_pos):
        #死
        pygame.quit()

    print(snake_init_pos)

def main():
    for pos in snake_init_pos:
        draw_rect(white_color, pos)

    draw_rect(white_color, food_pos)
    pygame.display.update()

    while 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    print ('左')
                    head_pos[0] -= cell
                    change_direction(head_pos)
                elif event.key == pygame.K_RIGHT:
                    print ('右')
                    head_pos[0] += cell
                    change_direction(head_pos)
                elif event.key == pygame.K_UP:
                    print ('上')
                    head_pos[1] -= cell
                    change_direction(head_pos)
                elif event.key == pygame.K_DOWN:
                    print ('下')
                    head_pos[1] += cell
                    change_direction(head_pos)


        #每操作一次键盘 更新位置，需要渲染一下画面
        caption.fill(black_color)
        draw_rect(white_color, food_pos)

        for pos in snake_init_pos:
            draw_rect(white_color, pos)

        pygame.display.update()
        clock.tick(10)

if __name__ == '__main__':
    main()
