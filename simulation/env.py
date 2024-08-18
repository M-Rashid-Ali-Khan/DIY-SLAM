# Tutorial taken from https://www.youtube.com/watch?v=JbUNsYPJK1U&list=PL9RPomGb9IpRJLw5UTdSy4eJeoLrwNcfC&index=2

import math,cv2,pygame
import numpy as np

class buildEnvironment:
    def __init__(self,map_template,mapWindowName,MapDimensionsWH):
        pygame.init()
        self.pointCloud=[]
        image = cv2.imread(map_template, cv2.IMREAD_GRAYSCALE)  # Use your image file path
        threshold = 128  # Adjust this value for different thresholding
        _, bw_image = cv2.threshold(image, threshold, 255, cv2.THRESH_BINARY)
        # bw_image = cv2.cvtColor(bw_image, cv2.COLOR_GRAY2RGB)  # Convert to RGB format
        cv2.imshow("Image",bw_image)
        bw_image = np.flip(bw_image, axis=0)  # Flip the image vertically (cv2 and pygame have different origins)
        bw_image = cv2.rotate(bw_image, cv2.ROTATE_90_CLOCKWISE)
        self.externalMap = pygame.surfarray.make_surface(bw_image)
        # self.externalMap = pygame.image.load(map_template)
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


