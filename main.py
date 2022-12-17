from algorithms.chan import *
from algorithms.grahams import *
from algorithms.increment import *
from algorithms.jarvis import *
from algorithms.quickhull import *
from algorithms.upperlowerhull import *

from utils.generate import *
from utils.viz import *

import copy
import time


# points = genUniformRectangle(-10, 10, -20, 30, 1000)
# points = genUniformCirle(10, 10, 10, 3)
# points = genUniformOnRectangle([-10, -10], [20, 30], 100)
# points = genUniformOnSquare(10, 20, 20)
hull = quickhull(points)
plotHull(points, hull)
