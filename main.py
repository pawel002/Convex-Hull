from convexhulls import *

# MIEJSCE DO TESTOWANIA FUNKCJI

# points1 = genUniformRectangle(-10, 10, -20, 30, 100)
# points2 = genUniformCircle(10, 10, 10, 100)
# points3 = genUniformOnRectangle(-10, 10, 20, 30, 100)
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

# sizes = [100, 1000, 10000, 100000, 1000000]
# functions = [divideconquer]

# hull = divideconquer(genUniformCircle(0, 0, 100, 100000))

# for f in functions:
#     for s in sizes:
#         benchmark(f, 5, genUniformOnSquare, 10, int(s/4), int(s/4))


# sizes = [100, 1000, 10000, 100000, 1000000]
# functions = [chan]

# for f in functions:
#     for s in sizes:
#         benchmark(f, 5, genUniformOnSquare, 10, int(s//4), int(s//4))

# benchmark(increment, 2, genUniformRectangle, -10, 10, -10, 10, 1000000)
# benchmark(increment, 2, genUniformRectangle, -10, 10, -10, 10, 10000)
