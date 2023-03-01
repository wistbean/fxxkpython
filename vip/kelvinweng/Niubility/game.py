import pygame
from pygame.locals import *
import random



caption_width = 300
caption_height = 600
game_title = '牛逼的黄瓜'

hero_width = 50
hero_height = 50

cucumber_width = 80
cucumber_height = 380

floor_width = caption_width
floor_height = 100

speed = 10 
space = 140

score = 0

class Hero(pygame.sprite.Sprite):


    def __init__(self,top=0):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('hero.png').convert_alpha()
        self.image = pygame.transform.scale(self.image,(hero_width,hero_height))
        self.rect = self.image.get_rect()
        self.rect.left = caption_width/2 - hero_width
        self.rect.top = caption_height/2 - hero_height - top
        self.speed = speed

    def update(self):
        self.speed += 1
        self.rect.top += self.speed

    def fly(self):
        self.speed = -speed


class Cucumber(pygame.sprite.Sprite):

    def __init__(self,change,left,top):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('cucumber.png').convert_alpha()
        self.image = pygame.transform.scale(self.image,(cucumber_width,cucumber_height))
        self.rect = self.image.get_rect()
        self.rect.left = left
        if change:
            self.image = pygame.transform.flip(self.image,False,True)
            self.rect.top = - (self.rect.bottom - top)
        else:
            self.rect.top = caption_height - top

    def update(self):
        self.rect.left -= speed



class Floor(pygame.sprite.Sprite):

    def __init__(self,left):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('floor.png').convert_alpha()
        self.image = pygame.transform.scale(self.image,(floor_width,floor_height))
        self.rect = self.image.get_rect()
        self.rect.left = left
        self.rect.top = caption_height - floor_height

def generate_Cucumber(left):
    top = random.randint(100,300)
    cucumber = Cucumber(False,left,top)
    cucumber_changed = Cucumber(True,left,caption_height - top - space)
    return cucumber,cucumber_changed

if __name__ == '__main__':
    pygame.init()
    game_font = pygame.font.SysFont('arial',16)
    caption = pygame.display.set_mode((caption_width,caption_height))
    pygame.display.set_caption(game_title)
    
    background = pygame.image.load('bg.png')
    background = pygame.transform.scale(background,(caption_width,caption_height))

    hero_group = pygame.sprite.Group()
    hero = Hero()
    hero_group.add(hero)

    floor_group = pygame.sprite.Group()
    floor = Floor(0)
    floor_group.add(floor)
    

    cucumber_group = pygame.sprite.Group()
    cucumbers1 = generate_Cucumber(300)
    cucumber_group.add(cucumbers1[0])
    cucumber_group.add(cucumbers1[1])

    clock = pygame.time.Clock()
    
    while True:
        clock.tick(25)
        caption.blit(background,(0,0))
        caption.blit(game_font.render('score:%d'%score,True,[0,0,0]),[20,20])

        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_SPACE:
                    hero.fly()
                    
        if cucumber_group.sprites()[0].rect.left < -(caption_width):
            cucumber_group.remove(cucumber_group.sprites())
            cucumbers = generate_Cucumber(caption_width)
            cucumber_group.add(cucumbers[0])
            cucumber_group.add(cucumbers[1])
            score += 1

        hero_group.update()        
        hero_group.draw(caption)    
        cucumber_group.update()
        cucumber_group.draw(caption)
        floor_group.draw(caption)
        pygame.display.update()

        #if pygame.sprite.groupcollide(hero_group,floor_group,False,False)\
        #       or pygame.sprite.groupcollide(hero_group,cucumber_group,False,False):
        #    pygame.quit()
        #    quit()
        
