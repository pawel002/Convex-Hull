from convexhulls import *

import copy
import time


# points1 = genUniformRectangle(-10, 10, -20, 30, 100)
# points2 = genUniformCirle(10, 10, 10, 100)
# points3 = genUniformOnRectangle(-10, -10, 20, 30, 100)
# points4 = genUniformOnSquare(10, 25, 25)

# plotPoints(points1)
# plotPoints(points2)
# plotPoints(points3)
# plotPoints(points4)

# bigPoints = genUniformOnRectangle([-10, -10], [20, 30], 10000)
# bigPoints = genUniformOnSquare(10, 500, 500)
# bigPoints = genUniformCirle(10, 10, 10, 1000)

# points = genUniformRectangle(-10, 10, -20, 30, 20)
# # hull = increment(points)
# # plotHull(points, hull)

# points = genUniformOnRectangle(-10, 10, -10, 10, 200)
# plotPoints(points)
# saveList(points1, "points1")
# points1 = readList("points1")
# # print(points1)
# plotPoints(points1)

# points = genUniformRectangle(-10, 10, -10, 10, 10)
# visHull(incrementVis, points)

sizes = [100, 1000, 10000, 100000, 1000000]
functions = [jarvis, grahams, quickhull, upperlower, increment]

for f in functions:
    for s in sizes:
        benchmark(f, 5, genUniformOnRectangle, -10, 10, -10, 10, s)


# sizes = [100000, 1000000]
# functions = [grahams, quickhull, upperlower, increment]

# for f in functions:
#     for s in sizes:
#         benchmark(f, 5, genUniformCircle, 0, 0, 10, s)

# benchmark(jarvis, 2, genUniformCirle, 10, 10, 10, 10000)
# benchmark(increment, 2, genUniformRectangle, -10, 10, -10, 10, 10000)
