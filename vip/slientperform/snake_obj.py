import pygame
import random

white_color = [255, 255, 255]
black_color = [0, 0, 0]
caption_width = 500
caption_height = 500
food_pos = [random.randrange(1, 50) * 10, random.randrange(1, 50) * 10]
cell = 10
game_title = '帅气的python'


class Snake():
    def __init__(self):
        self.head_pos = [250, 250]
        self.position = [[250, 250], [240, 250], [230, 250], [220, 250]]

    def hit_wall(self):
        if self.head_pos[0] >= caption_width or self.head_pos[0] < 0 or self.head_pos[1] >= caption_height or \
                self.head_pos[1] < 0:
            return True
        else:
            return False

    def hit_self(self):
        if self.position[0] in self.position[1:]:
            return True
        else:
            return False

    def change_direction(self):
        global food_pos
        self.position.insert(0, list(self.head_pos))
        if self.position[0] != food_pos:
            self.position.pop()
        else:
            food_pos = [random.randrange(1, 50) * 10, random.randrange(1, 50) * 10]
        if self.hit_self() or self.hit_wall():
            pygame.quit()


def main():
    pygame.init()  # 初始化 pygame
    clock = pygame.time.Clock()

    caption = pygame.display.set_mode((caption_width, caption_height))
    pygame.display.set_caption(game_title)

    def draw_rect(color, position):
        pygame.draw.rect(caption, color, pygame.Rect(position[0], position[1], cell, cell))

    snake = Snake()
    for pos in snake.position:
        draw_rect(white_color, pos)

    draw_rect(white_color, food_pos)
    pygame.display.update()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    snake.head_pos[0] -= cell
                    snake.change_direction()
                if event.key == pygame.K_RIGHT:
                    snake.head_pos[0] += cell
                    snake.change_direction()
                if event.key == pygame.K_UP:
                    snake.head_pos[1] -= cell
                    snake.change_direction()
                if event.key == pygame.K_DOWN:
                    snake.head_pos[1] += cell
                    snake.change_direction()

        caption.fill(black_color)
        draw_rect(white_color, food_pos)

        for pos in snake.position:
            draw_rect(white_color, pos)

        pygame.display.update()
        clock.tick(10)


if __name__ == '__main__':
    main()