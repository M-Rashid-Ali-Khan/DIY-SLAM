import pygame
import math
import numpy as np

class LaserSensor:
    def __init__(self,range,map,position:tuple[int,int],envSize:tuple[int,int],
                    sampleRate = 60, speed = 4):
        self.noise_func = None
        self.sampleRate = sampleRate
        self.range = range
        self.speed = speed #rounds per second
        self.sigma = None
        self.position = position
        self.map = map
        self.envW,self.envH = envSize
        self.sensedObstacles = []
    
    def distance(self,obstaclePosition:tuple[int,int]):
        px = (obstaclePosition[0]-self.position[0])**2
        py = (obstaclePosition[1]-self.position[1])**2
        return math.sqrt(px+py)

    def sense_obstacle(self):
        data = []
        x1,y1 = self.position[0],self.position[1]
        for angle in np.linspace(0,2*math.pi,self.sampleRate,False):
            x2,y2 = (x1 + self.range*math.cos(angle), y1 - self.range*math.sin(angle))
            for i in range(0,100):
                u = i/100.0
                x = int(x1*(1-u) + x2*u)
                y = int(y1*(1-u) + y2*u)
                if x>=self.envW or y>=self.envH:
                    break
                #TODO: Add size of lidar...currently it takes one box
                if x>0 and y>0:
                    color = self.map.get_at((x,y))
                    if (color[0],color[1],color[2]) == (0,0,0):
                        distance = self.distance((x,y))
                        if self.noise_func != None:
                            output = self.noise_func(distance,angle,self.sigma)
                            output.append(self.position)
                        else:
                            output = [distance,angle,self.position]
                        data.append(output)
                        break
        if len(data)>0:
            return data
        else:
            return None

    def add_noise(self,uncertainity: tuple[float, float],noise_func):
        self.noise_func = noise_func
        self.sigma = np.array([uncertainity[0],uncertainity[1]])



              


