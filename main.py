from simulation import env,sensors
from simulation import data_manipulation as dm
import pygame
import math

environment = env.buildEnvironment('assets/floor2.png','SLAM PLanning',(600,400))
environment.originalMap = environment.map.copy()
envSize = pygame.display.get_surface().get_size()
laser = sensors.LaserSensor(200,environment.originalMap,(0,0),envSize)
laser.add_noise((0.5,0.01),dm.add_uncertainity)
# environment.map.fill((0,0,0))
environment.infomap = environment.map.copy()
running = True

while running:
    SensorON = False
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if pygame.mouse.get_focused():
            SensorON = True
        elif  not pygame.mouse.get_focused():
            SensorON = False
    if SensorON:
        position = pygame.mouse.get_pos()
        laser.position = position
        sensorData = laser.sense_obstacle()
        sensorData = dm.relPolar2absCart(sensorData)
        environment.dataStorage(sensorData)
        environment.show_sensorData()
    environment.map.blit(environment.infomap,(0,0))
    pygame.display.update()


    
    pygame.display.update()
