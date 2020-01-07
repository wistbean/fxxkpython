import random
import pygame

caption_width = 500
caption_height = 500
white_color = (255, 255, 255)
black_color = (0, 0, 0)
green_color = (0, 255, 0)
game_title = '绿头蛇'
snake_pos = [[250, 250], [240, 250], [230, 250], [220, 250]]
food_pos = [random.randrange(1, 50) * 10, random.randrange(1, 50) * 10]
cell = 10
head_pos = [250, 250]
score = 0
score_pos = (415, 20)
end_pos = (250, 250)

pygame.init()
pygame.font.init()
clock = pygame.time.Clock()

pygame.display.set_caption(game_title)
caption = pygame.display.set_mode((caption_width, caption_height))

score_font = pygame.font.SysFont('pingfangttc', 20, True)
end_font = pygame.font.SysFont('pingfangttc', 40, True)

def draw_rect(color, position):
    pygame.draw.rect(caption, color, pygame.Rect(position[0], position[1], cell, cell))

def hit_the_self():
    if snake_pos[0] in snake_pos[1:]:
        return  True
    else:
        return False

def hit_the_wall():
    if head_pos[0] >= 500 or head_pos[0] <= 0 or head_pos[1] >= 500 or head_pos[1] <=0:
        return True
    else:
        return False

def change_dirction(head_pos):
    global food_pos
    global score
    snake_pos.insert(0, list(head_pos))
    if head_pos != food_pos:
        snake_pos.pop()
    else:
        food_pos = [random.randrange(1, 50) * 10, random.randrange(1, 50) * 10]
        score += 1
        print(score)

    if hit_the_self() or hit_the_wall():                                        # 游戏结束界面未完成
        end_text = end_font.render('Game Over!', True, green_color)
        end_rect = end_text.get_rect()
        end_rect.center = end_pos
        caption.blit(end_text, end_rect)
        pygame.display.update()
        pygame.time.wait(500)
        pygame.quit()

def main():
    for pos in snake_pos[1:]:
        draw_rect(white_color, pos)
        draw_rect(green_color, snake_pos[0])
    draw_rect(white_color, food_pos)
    pygame.display.update()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    print('left')
                    head_pos[0] -= cell
                    change_dirction(head_pos)
                elif event.key == pygame.K_RIGHT:
                    print('right')
                    head_pos[0] += cell
                    change_dirction(head_pos)
                elif event.key == pygame.K_UP:
                    print('up')
                    head_pos[1] -= cell
                    change_dirction(head_pos)
                elif event.key == pygame.K_DOWN:
                    print('down')
                    head_pos[1] += cell
                    change_dirction(head_pos)

        caption.fill(black_color)
        for pos in snake_pos[1:]:
            draw_rect(white_color, pos)
            draw_rect(green_color, snake_pos[0])
        draw_rect(white_color, food_pos)

        score_text = score_font.render('Your Score: {}'.format(score), True, white_color)
        score_rect = score_text.get_rect()
        score_rect.center = score_pos
        caption.blit(score_text, score_rect)

        pygame.display.update()
        clock.tick(10)

if __name__ == '__main__':
    main()



