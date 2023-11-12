import pygame
from sys import exit

pygame.init()
screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption('Hello PyGame')
clock = pygame.time.Clock()
test_font = pygame.font.Font('font/Pixeltype.ttf', 50)

sky_surface = pygame.image.load('graphics/Sky.png').convert()
ground_surface = pygame.image.load('graphics/Ground.png').convert()
text_surface = test_font.render('My PyGame', False, 'Black')

snail_surface = pygame.image.load('graphics/snail/Snail1.png').convert_alpha()
snail_x_pos = 800

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    screen.blit(sky_surface, (0, 0))
    screen.blit(ground_surface, (0, 300))
    screen.blit(text_surface, (300, 50))

    snail_x_pos -= 3
    if snail_x_pos < 0-72:
        snail_x_pos = 800
    screen.blit(snail_surface, (snail_x_pos, 300-36))

    pygame.display.update()
    clock.tick(60)