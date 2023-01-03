from algorithms.helpers import length, orient #1 = ccw, -1 = cw
from algorithms.grahams import grahams
from utils.viz import *
from utils.generate import *
from math import atan2, pi
from functools import reduce

def angle(a, b, c): #clockwise angle by turning from a to c around b
    if a==b or b==c or c==b: return 0
    ang = atan2(a[1]-b[1], a[0]-b[0]) - atan2(c[1]-b[1], c[0]-b[0]) 
    return ang + 2*pi if ang < 0 else ang
    

def isLeft(a,b,c):
    return (b[0] - a[0])*(c[1] - a[1]) - (c[0] - a[0])*(b[1]-a[1])
def above (p,vi,vj):
    return(isLeft(p,vi,vj) > 0)
def below(p,vi,vj):
    return(isLeft(p,vi,vj) < 0)

def rTanToSeg(p, hull):
    if orient(p, hull[0], hull[1]) == 1: return 0
    if orient(p, hull[0], hull[1]) == -1: return 1
    
    return 0 if length(p, hull[0]) > length(p, hull[1]) else 1

def rightTangent(p, n, V):

    if (below(p, V[1], V[0])) and (not above(p, V[n-1], V[0])): return 0
    if (above(p, V[n-1], V[n-2])) and (not below(p, V[n-1], V[0])): return n-1
    a, b = 0, n
    if orient(V[a], p, V[b-1]) == 0: 
            return a if orient(p, V[a], V[a+1]) == 1 else b-1
    while True:    
        if p == V[a]: return a+1
        if p == V[b]: return b+1
        #if orient(p, V[a], V[a+1]) == 1  and orient(p, V[a], V[a-1]) > -1: return a

        c = (a+b)//2
        dnC = below(p, V[c+1], V[c])
        if (dnC and (not above(p, V[c-1], V[c]))): return c
        if c == a: 
            return rTanToSeg(p, V[a:b+1])

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

def compute(points, m):
    eps = 10**(-10)
    count = 0
    idx = -1
    hulls_ = []
    for x in points:
        if count == 0: 
            hulls_.append([])
            idx += 1
        hulls_[idx].append(x)
        count = (count+1)%m
    hulls = [grahams(x) for x in hulls_]

    p = max(points)
    p0 = [p[0] + 10, p[1]]
    stack = [p0, p]
    for k in range(m):
        ang = -float('inf')
        leng = 0
        point = None

        for hull in hulls:
            n = len(hull)

            if n == 1: currIdx = 0
            elif n == 2: currIdx = rTanToSeg(stack[-1], hull)
            else:      
                currIdx = rightTangent(stack[-1], n ,hull+[hull[0]])%n
                if orient(stack[-1], hull[currIdx], hull[(currIdx+1)%n]) == 0: currIdx = (currIdx+1)%n
            curr = hull[currIdx]
            if curr == stack[-1]: curr = hull[(currIdx + 1)%len(hull)]
            
            angl = angle(stack[-2], stack[-1], curr)

            if angl > ang or (ang - eps <= angl <= ang+ eps and length(curr, stack[-1]) > leng):
                ang = angl 
                point = curr
                leng = length(curr, stack[-1]) 

            if point == stack[1]: 
                stack = stack[1:]
                return stack
        stack.append(point)
    
    return None

def chan(points):
    n = len(points)
    for i in range(1, n):
        m = min(2**(2**i), n)
        L = compute(points, m)
        if L is not None: return L

############ VIS #############

def computeVis(points, m, scenes):
    eps = 10**(-10)
    count = 0
    idx = -1
    hulls_ = []
    for x in points:
        if count == 0: 
            hulls_.append([])
            idx += 1
        hulls_[idx].append(x)
        count = (count+1)%m
    hulls = [grahams(x) for x in hulls_]

    linesStart = []
    for x in hulls:
        linesStart.append( [[x[i-1], x[i]] for i in range(len(x))] )
    hullStart = reduce(lambda a ,b: a+b, hulls)
    linesa = [LinesCollection(x, color='black') for x in linesStart]
    pointsa = [PointsCollection(hullStart, color='red')]
    scenes.append(Scene(pointsa, linesa))


    p = max(points)
    p0 = [p[0] + 10, p[1]]
    stack = [p0, p]
    for k in range(m):
        currTab = []
        ang = -float('inf')
        leng = 0
        point = None
        tangents = []
        for hull in hulls:
            n = len(hull)

            if n == 1: currIdx = 0
            elif n == 2: currIdx = rTanToSeg(stack[-1], hull)
            else:      
                currIdx = rightTangent(stack[-1], n ,hull+[hull[0]])%n
                if orient(stack[-1], hull[currIdx], hull[(currIdx+1)%n]) == 0: currIdx = (currIdx+1)%n
            curr = hull[currIdx]
            if curr == stack[-1]: curr = hull[(currIdx + 1)%len(hull)]
            currTab.append(curr)
            
            angl = angle(stack[-2], stack[-1], curr)

            if angl > ang or (ang - eps <= angl <= ang+ eps and length(curr, stack[-1]) > leng):
                ang = angl 
                point = curr
                leng = length(curr, stack[-1]) 

            tangents.append([stack[-1], curr])
        stacky = stack[1:] if len(stack) > 1 else [(10,-10), stack[0]]
        pointsy = [pointsa[0], PointsCollection(stacky, color = 'yellow'), PointsCollection([point], color='pink', zorder = 3, s=40), \
            PointsCollection(currTab, color = 'lime', zorder = 2)]  
        newlines = linesa + [LinesCollection([[stacky[i-1] , stacky[i]] for i in range(len(stacky))], color= 'purple'), LinesCollection(tangents, color='blue', zorder=10)]

        scenes.append(Scene(pointsy, newlines))
        if point == stack[1]: 
            stack = stack[1:]
            newlines = [LinesCollection([[stack[i-1], stack[i]] for i in range(len(stack))], color='black')]
            pointsy = [PointsCollection(points), PointsCollection(stack, color = 'red')]
            scenes.append(Scene(pointsy, newlines))

            return stack[1:]
        stack.append(point)
    
    return None

def chanVis(points):
    n = len(points)
    scenes = [Scene([PointsCollection(points)])]
    for i in range(1, n):
        m = min(2**(2**i), n)
        L = computeVis(points, m, scenes)
        if L is not None: 
            return scenes