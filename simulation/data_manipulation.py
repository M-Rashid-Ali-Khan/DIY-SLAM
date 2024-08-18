import numpy as np
import math

def add_uncertainity(distance,angle,sigma):
    mean = np.array([distance,angle])
    covariance = np.diag(sigma**2)
    distance,angle = np.random.multivariate_normal(mean,covariance)
    distance = max(distance,0)
    if angle < 0:
      angle = 2*math.pi - angle  
    return [distance,angle]

def polar2cart(data:list[any,any,any]):
    radius = data[0]
    angle = data[1]
    x = radius * math.cos(angle)
    y = -radius * math.sin(angle)
    data[0] = x
    data[1] = y
    return data

def rel2absPos(x,y,robotPosition):
    x = x + robotPosition[0]
    y = y + robotPosition[1]
    return ( int(x),int(y) )

def relPolar2absCart(dataList:list|None):
    if dataList == None:
        return None
    cartList = []
    for element in dataList:
        element = polar2cart(element)
        cartList.append(rel2absPos(element[0],element[1],element[2]))
    return cartList