from algorithms.helpers import *
from utils.viz import *

from functools import cmp_to_key

def grahamsCmp(a, b, c):
    val = orient(a, b, c)
    if val != 0:
        return val
    if lengthSquared(a, b) >= lengthSquared(a, c):
        return 1
    return -1

def grahams(points):
    '''GRAHAMS'''

    startpPoint = min(points, key=lambda x: (x[1], x[0]))

    start = points.pop(points.index(startpPoint))

    points.sort(key=cmp_to_key(lambda x, y : grahamsCmp(start, y, x)))

    hull = [start] + points[:2]

    i = 2
    while i < len(points):

        val = orient(hull[-2], hull[-1], points[i])       

        if val == 0:
            hull.pop(-1)
            hull.append(points[i])
            i += 1    
        elif val == 1:
            hull.append(points[i])
            i += 1
        else:
            hull.pop(-1)

    if orient(hull[-2], hull[-1], hull[0]) == 0:
        hull.pop(-1)

    return hull


def grahamsVis(points):
    '''GRAHAMS VISUALIZATION'''

    scenes = []

    startpPoint = min(points, key=lambda x: (x[1], x[0]))

    start = points.pop(points.index(startpPoint))

    points.sort(key= cmp_to_key(lambda x, y : grahamsCmp(start, y, x)))

    hull = [start] + points[:2]

    i = 2
    while i < len(points):            
        if orient(hull[-2], hull[-1], points[i]) == 0:
            hull.pop()
            hull.append(points[i])
            i = i + 1    
        elif orient(hull[-2], hull[-1], points[i]) == 1:
            hull.append(points[i])
            i = i + 1
        else:
            hull.pop()
        
        scenes.append(Scene([PointsCollection(points, color="blue"), PointsCollection([point for point in hull], color='red', marker = "o")], [LinesCollection([[hull[i], hull[i+1]] for i in range(len(hull)-1)], color='red')])) 

    if orient(hull[-2], hull[-1], hull[0]) == 0:
        hull.pop()
    
    hull.append(hull[0])
    scenes.append(Scene([PointsCollection(points, color="blue"), PointsCollection([point for point in hull], color='red', marker = "o")], [LinesCollection([[hull[i], hull[i+1]] for i in range(len(hull)-1)], color='red')])) 

    return scenes
