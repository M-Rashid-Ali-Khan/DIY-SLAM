# Tutorial taken from https://www.youtube.com/watch?v=JbUNsYPJK1U&list=PL9RPomGb9IpRJLw5UTdSy4eJeoLrwNcfC&index=2

import math
import pygame

class buildEnvironment:
    def __init__(self,map_template,mapWindowName,MapDimensionsWH):
        pygame.init()
        self.pointCloud=[]
        self.externalMap = pygame.image.load(map_template)
        self.mapW,self.mapH = MapDimensionsWH
        self.mapWindowName = mapWindowName
        pygame.display.set_caption(self.mapWindowName)
        self.map = pygame.display.set_mode((self.mapW,self.mapH))
        self.map.blit(self.externalMap,(0,0))
        self.black = (0,0,0)
        self.grey = (70,70,70)
        self.blue = (0,0,255)
        self.green = (0,255,0)
        self.red = (255,0,0)
        self.white = (255,255,255)
    
    def dataStorage(self,data:tuple[(any,any)]|None):
        if data == None:
            return
        for point in data:
            if point not in self.pointCloud:
                self.pointCloud.append(point)

    def show_sensorData(self):
        self.infomap = self.map.copy()
        for point in self.pointCloud:
            self.infomap.set_at(point,self.red)


