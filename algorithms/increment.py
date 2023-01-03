# from algorithms.helpers import orient           

# from utils.viz import *

# def increment(points):

#     sorted_points = sorted([p for p in points])
#     hull = [sorted_points.pop(0)]

#     for i, p in enumerate(sorted_points):
#         if i+1 == len(sorted_points):
#             hull.append(sorted_points[-1])
#             break
#         elif orient(hull[0], p, sorted_points[i+1]) != 0:
#             hull.append(p)
#             sorted_points = sorted_points[i+1:]
#             break

#     while sorted_points:

#         curr = sorted_points.pop(0)
#         n = len(hull)

#         for i, left in enumerate(hull): #1 = ccw, -1 = cw
#             next = hull[(i+1)%n]
#             if orient(curr, left, next) != 1: 
#                 leftmost = i
#                 break

#         for i in range(leftmost, leftmost+n):
#             i = i%n 
#             right = hull[i]
#             next = hull[(i+1)%n]
#             if orient(curr, right, next) == 1:
#                 rightmost = i
#                 break
 
#         if orient(hull[leftmost], hull[rightmost], curr) == 0: 
#             hull = [hull[leftmost], curr]
#         elif leftmost < rightmost:      
#             hull = hull[:leftmost + 1] + [curr] + hull[rightmost:]
#         else: 
#             hull  = hull[rightmost:leftmost+1] + [curr] 

#     return hull


# def incrementVis(points):
#     ### viz
#     scenes = [Scene([PointsCollection(points)])]
#     ### end viz
#     sorted_points = sorted([p for p in points])
#     hull = [sorted_points.pop(0)]
#     for i, p in enumerate(sorted_points):
#         if i+1 == len(sorted_points):
#             hull.append(sorted_points[-1])
#             break
#         elif orient(hull[0], p, sorted_points[i+1]) != 0:
#             hull.append(p)
#             sorted_points = sorted_points[i+1:]
#             break
#     while sorted_points:
#         ### viz
#         lines = []
#         for i in range(len(hull)):
#             lines.append([hull[i], hull[(i+1)%len(hull)]])
#         scenes.append(Scene([PointsCollection(points), PointsCollection(hull, color='black',zorder=5)], [LinesCollection(lines, color='black', zorder=2)]))
#         ### end viz

#         curr = sorted_points.pop(0)
#         n = len(hull)

#         for i, left in enumerate(hull): #1 = ccw, -1 = cw
#             next = hull[(i+1)%n]
#             if orient(curr, left, next) != 1: 
#                 leftmost = i
#                 break

#         for i in range(leftmost, leftmost+n):
#             i = i%n 
#             right = hull[i]
#             next = hull[(i+1)%n]
#             if orient(curr, right, next) == 1:
#                 rightmost = i
#                 break
#         ### viz
#         scenes.append(Scene([PointsCollection(points), PointsCollection(hull, color='black',zorder=5)], [LinesCollection(lines, color='black', zorder=2), \
#             LinesCollection([[curr, hull[leftmost]]], color='red', zorder=4,linewidth=2), LinesCollection([[curr, hull[rightmost]]], color='green', zorder=4,linewidth=1.3)]))
#         ### end viz  
#         if orient(hull[leftmost], hull[rightmost], curr) == 0: 
#             hull = [hull[leftmost], curr]
#         elif leftmost < rightmost:      
#             hull = hull[:leftmost + 1] + [curr] + hull[rightmost:]
#         else: 
#             hull  = hull[rightmost:leftmost+1] + [curr] 
#     ### viz
#     lines = []
#     for i in range(len(hull)):
#         lines.append([hull[i], hull[(i+1)%len(hull)]])
#     scenes.append(Scene([PointsCollection(points), PointsCollection(hull, color='black',zorder=5)], [LinesCollection(lines, color='black', zorder=2)]))   
#     ### end viz 

#     return scenes

from algorithms.helpers import orient           

from utils.viz import *

def isLeft(a,b,c):
    return (b[0] - a[0])*(c[1] - a[1]) - (c[0] - a[0])*(b[1]-a[1])
def above (p,vi,vj):
    return(isLeft(p,vi,vj) > 0)
def below(p,vi,vj):
    return(isLeft(p,vi,vj) < 0)

def rightTangent(p, n, V):
    if (below(p, V[1], V[0])) and (not above(p, V[n-1], V[0])): return 0
    a, b = 0, n
    while True:
        c = (a+b)//2
        dnC = below(p, V[c+1], V[c])
        if (dnC and (not above(p, V[c-1], V[c]))): return c

        upA = above(p,V[a+1], V[a])
        if(upA):
            if(dnC): 
                b = c
            else:
                if above(p,V[a], V[c]):
                    b = c
                else:
                    a = c
        else:
            if (not dnC):
                a = c
            else:
                if (below(p, V[a], V[c])):
                    b = c
                else:
                    a = c

def leftTangent(p, n, V):

    if (not below(p, V[1], V[0])) and (above(p, V[n-1], V[0])): return 0
    a, b = 0, n
    while True:
        c = (a+b)//2
        dnC = below(p, V[c+1], V[c])
        if ((not dnC) and above(p, V[c-1], V[c])): return c

        dnA = below(p, V[a+1], V[a])
        if(dnA):
            if(not dnC): 
                b = c
            else:
                if below(p,V[a], V[c]):
                    b = c
                else:
                    a = c
        else:
            if (dnC):
                a = c
            else:
                if (above(p, V[a], V[c])):
                    b = c
                else:
                    a = c


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

        leftmost = leftTangent(curr, n, hull + [hull[0]])%n

        rightmost = rightTangent(curr, n, hull + [hull[0]])%n
        if n > 2:
            while orient(curr, hull[rightmost], hull[(rightmost+1)%n]) == 0:
                rightmost = (rightmost+1)%n
 
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

        leftmost = leftTangent(curr, n, hull + [hull[0]])%n

        rightmost = rightTangent(curr, n, hull + [hull[0]])%n
        if n > 2:
            while orient(curr, hull[rightmost], hull[(rightmost+1)%n]) == 0:
                rightmost = (rightmost+1)%n

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