from algorithms.helpers import *

def quickHullRecursive(p1, p2, points):
    if not points:
        return []

    farthest = max(points, key=lambda p: det(p1, p2, p))

    hull = [farthest]

    leftPoints = [p for p in points if p != farthest and det(p1, farthest, p) > 0]
    rightPoints = [p for p in points if p != farthest and det(farthest, p2, p) > 0]

    left_hull = quickHullRecursive(p1, farthest, leftPoints)
    right_hull = quickHullRecursive(farthest, p2, rightPoints)

    hull = right_hull + hull + left_hull
    return hull


def quickhull(points):
    leftmost = min(points)
    rightmost = max(points)

    hull = [leftmost, rightmost]

    leftPoints = [p for p in points if p != leftmost and p != rightmost and det(leftmost, rightmost, p) > 0]
    rightPoints = [p for p in points if p != leftmost and p != rightmost and det(leftmost, rightmost, p) < 0]

    left_hull = quickHullRecursive(leftmost, rightmost, leftPoints)
    right_hull = quickHullRecursive(rightmost, leftmost, rightPoints)

    hull = left_hull + [hull[0]] + right_hull + [hull[1]]

    return hull

def quickhullVis(points):
    pass

