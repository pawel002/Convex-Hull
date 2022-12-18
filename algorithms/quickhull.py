from algorithms.helpers import *
from utils.viz import *

def quickHullRecursive(p1, p2, points):
    if not points:
        return []

    farthest = max(points, key=lambda p: det(p1, p2, p))

    hull = [farthest]

    leftPoints = [p for p in points if p != farthest and det(p1, farthest, p) > 0]
    rightPoints = [p for p in points if p != farthest and det(farthest, p2, p) > 0]

    leftHull = quickHullRecursive(p1, farthest, leftPoints)
    rightHull = quickHullRecursive(farthest, p2, rightPoints)

    hull = rightHull + hull + leftHull
    return hull


def quickhull(points):
    leftmost = min(points)
    rightmost = max(points)

    hull = [leftmost, rightmost]

    leftPoints = [p for p in points if p != leftmost and p != rightmost and det(leftmost, rightmost, p) > 0]
    rightPoints = [p for p in points if p != leftmost and p != rightmost and det(leftmost, rightmost, p) < 0]

    leftHull = quickHullRecursive(leftmost, rightmost, leftPoints)
    rightHull = quickHullRecursive(rightmost, leftmost, rightPoints)

    hull = leftHull + [hull[0]] + rightHull + [hull[1]]

    return hull

def quickhullVis(points):

    scenes = []
    leftmost = min(points)
    rightmost = max(points)

    hull = [leftmost, rightmost]
    scenes.append(Scene([PointsCollection(points, color="blue"),
                     PointsCollection([point for point in hull], color='red', marker = "o")],
                    [LinesCollection([[hull[i], hull[i+1]] for i in range(len(hull)-1)], color='red')]))
    
    prevhulls = []

    leftPoints = [p for p in points if p != leftmost and p != rightmost and det(leftmost, rightmost, p) > 0]
    rightPoints = [p for p in points if p != leftmost and p != rightmost and det(leftmost, rightmost, p) < 0]

    que = [(leftmost, rightmost, leftPoints), (rightmost, leftmost, rightPoints)]

    while que:

        p1, p2, currPoints = que.pop(0)
        if not currPoints:
            continue

        farthest = max(currPoints, key=lambda p: det(p1, p2, p))
        hull.insert(hull.index(p2), farthest)

        prevhulls.append([p1, p2])

        leftPoints = [p for p in points if p != farthest and det(p1, farthest, p) > 0]
        rightPoints = [p for p in points if p != farthest and det(farthest, p2, p) > 0]

        que.append((p1, farthest, leftPoints)) 
        que.append((farthest, p2, rightPoints))


        scenes.append(Scene([PointsCollection(points, color="blue"),
                    PointsCollection([point for point in hull], color='red', marker = "o", zorder=3)],
                    [LinesCollection([[hull[i], hull[i+1]] if i < len(hull) - 1 else [hull[i], hull[0]] for i in range(len(hull))], color='red', zorder=3),
                     LinesCollection([line for line in prevhulls], color='gray')]))

    return scenes

