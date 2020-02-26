import pygame
import random
caption_width=500 #设置宽度
caption_height=500 #设置高度
white_color = (255,255,255)#白色RGB
black_color = (0,0,0)
game_title = "rush_B贪吃蛇"
cell = 10#格子
snake_init_pos=[[250,250],[240,250],[230,250],[220,250]] #蛇初始位置
food_pos = [random.randrange(1,50)*10,random.randrange(1,50)*10] #食物的初始位置
head_pos = [250,250]#定义蛇头位置

pygame.init() #初始化pygame
clock = pygame.time.Clock()

caption=pygame.display.set_mode((caption_width,caption_height)) # 设置画布    pygame.display.set_mode初始化一个准备显示的窗口或屏幕 
pygame.display.set_caption(game_title) #设置标题

def draw_rect(color,postion):#创建绘制矩形方法
    pygame.draw.rect(caption, color, pygame.Rect(postion[0],postion[1],cell,cell))#绘制矩阵
    #pygame.draw.rect(Surface, color, Rect(left,top,width,height))
    #在Surface对像上绘制一个矩形 可以理解为在caption画布绘制矩形
def hit_the_self(): # 判断撞到自己
    #利用蛇头元素，和列表其他元素(身子)对比
    if snake_init_pos[0] in snake_init_pos[1:]: 
        print("撞到自己")
        return True
    else:
        return False
def hit_the_wall():#判断装墙
    #通过蛇头和画布范围对比
    if head_pos[0] >= caption_width or head_pos[0]<0 or head_pos[1]>=caption_height or head_pos[1]<0:
        print("撞到墙")
        return True
    else:
       
        return False


def change_direction(head_pos):
    global food_pos
    snake_init_pos.insert(0,list(head_pos))
    if head_pos != food_pos: # 蛇没有吃到食物，移动删除尾巴的矩形
        snake_init_pos.pop()
    else:
        food_pos =  [random.randrange(1,50)*10,random.randrange(1,50)*10] #吃到食物 重新生成食物
    if hit_the_self() or hit_the_wall(): #死
        pygame.quit()
    print(snake_init_pos)

def main():
    for pos in snake_init_pos:
        draw_rect(white_color,pos)
    draw_rect(white_color,food_pos)
    pygame.display.update()

    while 1:  #pygame.event.get 监听方向键 
        for event in pygame.event.get(): 
            if event.type == pygame.QUIT:#判断是否点击了关闭按钮
                pygame.quit()#卸载所有pygame模块
            
            #根据触发方向键，蛇头位置发生变化 更新蛇身的位置
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    print('左')
                    head_pos[0] -=cell
                    change_direction(head_pos)
                elif event.key == pygame.K_RIGHT:
                    print('右')
                    head_pos[0] +=cell
                    change_direction(head_pos)
                elif event.key == pygame.K_UP:
                    print('上')
                    head_pos[1] -=cell
                    change_direction(head_pos)
                elif event.key == pygame.K_DOWN:
                    print('下')
                    head_pos[1] +=cell
                    change_direction(head_pos)
        #每次更新 渲染一下画布 重新绘制画布
        caption.fill(black_color)
        draw_rect(white_color, food_pos)
       
        for pos in snake_init_pos:
            draw_rect(white_color, pos)
       
        pygame.display.update()
        clock.tick(10)#每秒循环十次 可以理解为每秒刷新10次


if __name__ == '__main__':
    main()



    
