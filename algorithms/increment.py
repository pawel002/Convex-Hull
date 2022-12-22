from algorithms.helpers import orient           

from utils.viz import *

def increment(points):

    sorted_points = sorted([p for p in points])
    hull = [sorted_points.pop(0)]

    for i, p in enumerate(sorted_points):
        if i+1 == len(sorted_points):
            hull.append(sorted_points[-1])
            break
        elif orient(hull[0], p, sorted_points[i+1]) != 0:
            hull.append(p)
            sorted_points = sorted_points[i+1:]
            break

    while sorted_points:

        curr = sorted_points.pop(0)
        n = len(hull)

        for i, left in enumerate(hull): #1 = ccw, -1 = cw
            next = hull[(i+1)%n]
            if orient(curr, left, next) != 1: 
                leftmost = i
                break

        for i in range(leftmost, leftmost+n):
            i = i%n 
            right = hull[i]
            next = hull[(i+1)%n]
            if orient(curr, right, next) == 1:
                rightmost = i
                break
 
        if orient(hull[leftmost], hull[rightmost], curr) == 0: 
            hull = [hull[leftmost], curr]
        elif leftmost < rightmost:      
            hull = hull[:leftmost + 1] + [curr] + hull[rightmost:]
        else: 
            hull  = hull[rightmost:leftmost+1] + [curr] 

    return hull


def incrementVis(points):
    ### viz
    scenes = [Scene([PointsCollection(points)])]
    ### end viz
    sorted_points = sorted([p for p in points])
    hull = [sorted_points.pop(0)]
    for i, p in enumerate(sorted_points):
        if i+1 == len(sorted_points):
            hull.append(sorted_points[-1])
            break
        elif orient(hull[0], p, sorted_points[i+1]) != 0:
            hull.append(p)
            sorted_points = sorted_points[i+1:]
            break
    while sorted_points:
        ### viz
        lines = []
        for i in range(len(hull)):
            lines.append([hull[i], hull[(i+1)%len(hull)]])
        scenes.append(Scene([PointsCollection(points), PointsCollection(hull, color='black',zorder=5)], [LinesCollection(lines, color='black', zorder=2)]))
        ### end viz

        curr = sorted_points.pop(0)
        n = len(hull)

        for i, left in enumerate(hull): #1 = ccw, -1 = cw
            next = hull[(i+1)%n]
            if orient(curr, left, next) != 1: 
                leftmost = i
                break

        for i in range(leftmost, leftmost+n):
            i = i%n 
            right = hull[i]
            next = hull[(i+1)%n]
            if orient(curr, right, next) == 1:
                rightmost = i
                break
        ### viz
        scenes.append(Scene([PointsCollection(points), PointsCollection(hull, color='black',zorder=5)], [LinesCollection(lines, color='black', zorder=2), \
            LinesCollection([[curr, hull[leftmost]]], color='red', zorder=4,linewidth=2), LinesCollection([[curr, hull[rightmost]]], color='green', zorder=4,linewidth=1.3)]))
        ### end viz  
        if orient(hull[leftmost], hull[rightmost], curr) == 0: 
            hull = [hull[leftmost], curr]
        elif leftmost < rightmost:      
            hull = hull[:leftmost + 1] + [curr] + hull[rightmost:]
        else: 
            hull  = hull[rightmost:leftmost+1] + [curr] 
    ### viz
    lines = []
    for i in range(len(hull)):
        lines.append([hull[i], hull[(i+1)%len(hull)]])
    scenes.append(Scene([PointsCollection(points), PointsCollection(hull, color='black',zorder=5)], [LinesCollection(lines, color='black', zorder=2)]))   
    ### end viz 

    return scenes