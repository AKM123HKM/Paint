import pygame,sys
from settings import *
from main_window import Window

pygame.init()

screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Paint App")
clock = pygame.time.Clock()
window = Window(screen)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        window.get_input(event)
        
    screen.fill(WHITE)
    window.run()
    pygame.display.update()
    clock.tick(FPS)