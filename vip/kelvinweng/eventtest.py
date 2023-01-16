import pygame

pygame.init()
pygame.display.set_caption('测试监听功能')
pygame.display.set_mode((500,500))

while 1:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                print('左')
            elif event.key == pygame.K_RIGHT:
                print('右')
            elif event.key == pygame.K_UP:
                print('上')
            elif event.key == pygame.K_DOWN:
                print('下')
        elif event.type == pygame.QUIT:
                pygame.quit()
