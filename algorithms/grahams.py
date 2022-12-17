from algorithms.helpers import *

from functools import cmp_to_key

def grahamsCmp(a, b, c):
    val = orient(a, b, c)
    if val != 0:
        return val
    if lengthSquared(a, b) >= lengthSquared(a, c):
        return 1
    return -1

def grahams(points):

    points.sort(key=lambda x:[x[1], x[0]])

    start = points.pop(0)

    points.sort(key= cmp_to_key(lambda x, y : grahamsCmp(start, y, x)))

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
