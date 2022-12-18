from algorithms.helpers import *
from utils.viz import *

def upperlower(points):

    points.sort()

    if len(points) <= 1:
        return points

    lower = []
    for p in points:
        while len(lower) >= 2 and det(lower[-2], lower[-1], p) <= 0:
            lower.pop()
        lower.append(p)

    upper = []
    for p in reversed(points):
        while len(upper) >= 2 and det(upper[-2], upper[-1], p) <= 0:
            upper.pop()
        upper.append(p)

    return lower[:-1] + upper[:-1]

def upperlowerVis(points):

    points.sort()
    scenes = []

    if len(points) <= 1:
        return points

    lower = []
    for p in points:
        while len(lower) >= 2 and det(lower[-2], lower[-1], p) <= 0:
            lower.pop()
            if lower:
                scenes.append(Scene([PointsCollection(points, color="blue"),
                         PointsCollection([point for point in lower], color='red', marker = "o")],
                        [LinesCollection([[lower[i], lower[i+1]] for i in range(len(lower)-1)], color='red')]))

        lower.append(p)
        scenes.append(Scene([PointsCollection(points, color="blue"),
                     PointsCollection([point for point in lower], color='red', marker = "o")],
                    [LinesCollection([[lower[i], lower[i+1]] for i in range(len(lower)-1)], color='red')]))

    upper = []
    for p in reversed(points):
        while len(upper) >= 2 and det(upper[-2], upper[-1], p) <= 0:
            upper.pop()
            if upper:
                scenes.append(Scene([PointsCollection(points, color="blue"),
                         PointsCollection([point for point in lower], color='red', marker = "o"),
                         PointsCollection([point for point in upper], color='green', marker = "o")],
                        [LinesCollection([[lower[i], lower[i+1]] for i in range(len(lower)-1)], color='red'),
                         LinesCollection([[upper[i], upper[i+1]] for i in range(len(upper)-1)], color='green')]))

        upper.append(p)
        scenes.append(Scene([PointsCollection(points, color="blue"),
                     PointsCollection([point for point in lower], color='red', marker = "o"),
                     PointsCollection([point for point in upper], color='green', marker = "o")],
                    [LinesCollection([[lower[i], lower[i+1]] for i in range(len(lower)-1)], color='red'),
                     LinesCollection([[upper[i], upper[i+1]] for i in range(len(upper)-1)], color='green')]))

    return scenes