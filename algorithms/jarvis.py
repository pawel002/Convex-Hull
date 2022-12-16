from algorithms.helpers import *

def jarvis(points):
    '''ALGORYTM JARVISA'''

    pointsCopy = [point for point in points]
    start = curr = min(pointsCopy, key=lambda x: (x[1], x[0]))

    hull = [curr]
    i = 0
    while True:
        print(hull)
        new = pointsCopy[0]

        for point in pointsCopy:
            if point == new or point == curr:
                continue

            d = orient(curr, new, point)

            if d == -1:
                new = point
            
            if d == 0 and lengthSquared(curr, point) > lengthSquared(curr, new):
                new = point

        if new == start:
            break
        
        hull.append(new)
        curr = new
    
    return hull
            

def jarvisVis(points):
    pass