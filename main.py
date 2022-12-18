from algorithms.chan import chan, chanVis
from algorithms.grahams import grahams, grahamsVis
from algorithms.increment import increment, incrementVis
from algorithms.jarvis import jarvis, jarvisVis
from algorithms.quickhull import quickhull, quickhullVis
from algorithms.upperlowerhull import upperlower, upperlowerVis

from utils.generate import *
from utils.viz import *
from utils.benchmark import *

import copy
import time


points = genUniformRectangle(-10, 10, -20, 30, 20)
# points = genUniformCirle(10, 10, 10, 100)
# points = genUniformOnRectangle([-10, -10], [20, 30], 100)
# points = genUniformOnSquare(10, 20, 20)

# hull = upperlower(points)
# plotHull(points, hull)

plot = Plot(jarvisVis(points))
plot.draw()

# benchmark(upperlower, 2, genUniformCirle, 10, 10, 10, 10000)
