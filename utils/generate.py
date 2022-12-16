from random import random
from math import cos, sin, pi

def lerp(a, b, t):
    return a + (b-a)*t

def genUniformRectangle(xStart, xEnd, yStart, yEnd, size):
    '''Generuje size punktów z prostokąta: xStart < x < xEnd i yStart < y < yEnd'''
    return [[lerp(xStart, xEnd, random()), lerp(yStart, yEnd, random())] for _  in range(size)]

def genUniformRectangle(x, y, radius, size):
    '''Generuje size punktów na okregu o środku w (x,y) i promieniu radius'''
    return [[x + radius*cos(angle), y + radius*cos(angle)] for angle in [2*pi*random() for _  in range(size)]]

def generate_set_c(lowerLeft, upperRight, size):
    '''Generuje size punktów na prostokącie o lewym dolnym punkcie w lowerLeft i prawym gowrnym upperRight.'''
    ll, ur, arr = lowerLeft, upperRight, [[] for _ in range(size)]
    for i in range(size):
        s = random.randint(0, 3)
        t = random.random()

        # dolna krawędz
        if s == 0:
            arr[i] = [lerp(ll[0], ur[0], t), ll[1]]
        
        # prawa krawędz
        if s == 1:
            arr[i] = [ur[0], lerp(ll[1], ur[1], t)]
        
        # górna krawędz
        if s == 2:
            arr[i] = [lerp(ll[0], ur[0], t), ur[1]]
        
        # lewa krawędz
        if s == 3:
            arr[i] = [ll[0], lerp(ll[1], ur[1], t)]
    
    return arr