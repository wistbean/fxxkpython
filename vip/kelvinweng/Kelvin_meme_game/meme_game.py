import sys
import pygame
from config import Config
from meme import Meme

class MemeGame:
    def __init__(self):
        pygame.init()
        self.config = Config()

        pygame.display.set_caption(self.config.game_title)

        self.screen = pygame.display.set_mode((self.config.screen_width,self.config.screen_height))

        self.meme = Meme(self)

    def _listen_event(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
                
    def _update_screen(self):
        self.screen.fill(self.config.screen_bg_color)
        
        
    def run_game(self):
        while True:
            self._listen_event()
            self._update_screen()
            self.meme.blit_meme()
            pygame.display.flip()

if __name__ == '__main__':
    meme_game = MemeGame()
    meme_game.run_game()
