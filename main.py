from simulation import env
import pygame
import math

environment = env.buildEnvironment('assets/floor2.png',(600,400))
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    pygame.display.update()
