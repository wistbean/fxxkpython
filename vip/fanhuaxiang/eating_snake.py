import random
import pygame


screen_width = 800 # 屏幕宽度
screen_height = 600 # 屏幕高度
color_white = (255, 255, 255) # 白蛇/白食
color_red = (255, 0, 0) # 红色
color_green = (0,255,0) # 绿色
length =12 # 蛇的初始长度
game_title = 'eating snake'
pixel = 10 # 像素块
snake_pos = []

def snake_positon(screen_width, screen_height, length, pixel): # 蛇初始位置及长度
    global snake_pos
    for i in range(length):
        pos = [int(screen_width/2+i*pixel), int(screen_height/2)]
        snake_pos.append(pos)
    return

snake_positon(screen_width, screen_height, length, pixel)
head_pos = [int(screen_width/2), int(screen_height/2)]# 蛇头初始位置

print(snake_pos)

food_pos = [random.randrange(pixel, screen_width, pixel), random.randrange(pixel, screen_height, pixel)] # 食儿初始位置，若不以piexl为单位，可能食物与蛇头不完全重合

pygame.init() # 初始化pygame
pygame.display.set_caption(game_title)
screen = pygame.display.set_mode((screen_width, screen_height))

def draw_rect(color, position):
    pygame.draw.rect(screen, color, pygame.Rect(position[0], position[1], pixel, pixel))

def eating_food(head_pos):
    global food_pos
    snake_pos.insert(0, list(head_pos))
    if head_pos == food_pos:
        food_pos = [random.randrange(pixel, screen_width, pixel), random.randrange(pixel, screen_height, pixel)]
    else:
        snake_pos.pop()
    print(snake_pos)

def eating_self():
    if snake_pos[0] in snake_pos[1:]:
        return  True
    else:
        return False

def hit_wall(head_pos):
    if head_pos[0] <= 0 or head_pos[0] >= screen_width or head_pos[1] <= 0 or head_pos[1] >= screen_width:
        return  True
    else:
        return False


while 1:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                print('left')
                head_pos[0] = head_pos[0] - pixel
                eating_food(head_pos)
            elif event.key == pygame.K_RIGHT:
                print('right')
                head_pos[0] = head_pos[0] + pixel
                eating_food(head_pos)
            elif event.key == pygame.K_UP:
                print('up')
                head_pos[1] = head_pos[1] - pixel
                eating_food(head_pos)
            elif event.key == pygame.K_DOWN:
                print('down')
                head_pos[1] = head_pos[1] + pixel
                eating_food(head_pos)
            elif event.key == pygame.K_ESCAPE:
                pygame.quit()
        if eating_self() or hit_wall(head_pos):
            print('Game Over')
            pygame.quit()

    screen.fill((0, 0, 0)) # 更新后重置画布，black(0, 0, 0)

    draw_rect(color_red, head_pos)
    for pos in snake_pos[1:]:
        draw_rect(color_white, pos)

    draw_rect(color_white, food_pos)
    pygame.display.update()





