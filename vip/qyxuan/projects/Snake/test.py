# -*-coding:utf-8 -*-
import pygame
import random

caption_name = "qyEatSnape"
white_color = (255,255,255)
black_color = (0,0,0)
cell = 10 #格子
cap_width = 500
cap_heigth = 500
snake_init_pos = [[250,250],[240,250],[230,250],[220,250]]
head_pos = [250,250]
food_pos = [random.randrange(1,50)*10, random.randrange(1,50)*10]

pygame.init()
clock = pygame.time.Clock()

caption = pygame.display.set_mode((cap_width,cap_heigth)) # ?
pygame.display.set_caption(caption_name)

def draw_rect(color,pos):
    pygame.draw.rect(caption, color, pygame.Rect(pos[0],pos[1], cell,cell))

def hit_the_self():
    if snake_init_pos[0] in snake_init_pos[1:]:
        return True
    else:
        return False

def hit_the_wall(head_pos):
    if head_pos[0] >= cap_width or head_pos[0] < 0 or head_pos[1] >= cap_heigth or head_pos[1] < 0:
        return True
    else:
        return False

def change_direction(head_pos):
    global food_pos # ? snap_init_pos 不需要加global
    snake_init_pos.insert(0, list(head_pos)) #吃到食物新增加一格

    if head_pos != food_pos:
        snake_init_pos.pop() #没吃到食物就跟踢除最后一格
    else:
        food_pos = [random.randrange(1,50)*10, random.randrange(1,50)*10]

    if hit_the_self() or hit_the_wall(head_pos):
        pygame.quit()



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
                    print('左')
                    head_pos[0] -= cell
                    change_direction(head_pos)
                elif event.key == pygame.K_RIGHT:
                    print('右')
                    head_pos[0] += cell
                    change_direction(head_pos)
                elif event.key == pygame.K_UP:
                    print('上')
                    head_pos[1] -= cell
                    change_direction(head_pos)
                elif event.key == pygame.K_DOWN:
                    print('下')
                    head_pos[1] += cell
                    change_direction(head_pos)

        caption.fill(black_color)
        draw_rect(white_color, food_pos)
        for pos in snake_init_pos:
            draw_rect(white_color, pos)

        pygame.display.update()
        clock.tick(10)

#加了这句，pygame窗口就不会闪退
if __name__ == '__main__':
    main()
