import pygame

class Meme():
    def __init__(self,meme_game):
        self.screen = meme_game.screen
        self.config = meme_game.config

        self.head = pygame.image.load(self.config.meme_head_image)
        self.head = pygame.transform.scale(self.head,self.config.meme_head_size)
        self.head_rect = self.head.get_rect()
        self.head_rect.center = self.screen.get_rect().center

        self.body_rect = pygame.Rect(
            0,
            0,
            self.config.meme_body_block_size,
            self.config.meme_body_block_size
        )

        self.len = 3
        self.body = [(0,0),(130,200),(160,200)]

        self.head_rect.x = 160
        self.head_rect.y = 0

        self.direction = 'k' #jkhl ----> 下上左右

    def blit_meme(self):
        for item in self.body:
            self.body_rect.x = item[0]
            self.body_rect.y = item[1]
            pygame.draw.rect(self.screen,self.config.meme_body_color,self.body_rect)
        self.screen.blit(self.head,self.head_rect)

    def move(self):
        head = self.body[0]
        if self.direction == 'k':
            now_head = (head[0],head[1]+30)
            self.body.insert(0,now_head)
            self.head_rect.x = now_head[0] - 15
            self.head_rect.y = now_head[1] + 15
