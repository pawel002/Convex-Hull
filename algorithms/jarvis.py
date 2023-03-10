from algorithms.helpers import *
from utils.viz import *

from functools import reduce

def min_angle(a, b, c):

    if a[0] == b[0] and a[1] == b[1]:
        return c
    if a[0] == c[0] and a[1] == c[1]:
        return b
        
    val = orient(a, b, c)

    if val == -1:
        return b
    elif val == 1:
        return c

    if lengthSquared(a, b) >= lengthSquared(a, c):
        return b
    return c

def jarvis(points):
    '''JARVIS'''

    start = min(points, key=lambda x: [x[1], x[0]])
    hull = [start]
    
    while True:
        point = reduce(lambda a, b: min_angle(start, a, b), points)
        start = point
        if hull[0] == point:
            break
        hull.append(point)
    
    return hull
            

def jarvisVis(points):
    '''JARVIS VISUALIZATION'''

    start = min(points, key=lambda x: [x[1], x[0]])
    hull = [start]
    scenes = []
    
    while True:
        scenes.append(Scene([PointsCollection(points, color="blue"),
                             PointsCollection([point for point in hull], color='red', marker = "o")],
                            [LinesCollection([[hull[i], hull[i+1]] for i in range(len(hull)-1)], color='red')]))
        
        point = reduce(lambda a, b: min_angle(start, a, b), points)
        start = point
        if hull[0] == point:
            break
        hull.append(point)
    
    hull.append(hull[0])
    scenes.append(Scene([PointsCollection(points, color="blue"),
                     PointsCollection([point for point in hull], color='red', marker = "o")],
                    [LinesCollection([[hull[i], hull[i+1]] for i in range(len(hull)-1)], color='red')]))
    
    return scenes