from algorithms.helpers import length, orient #1 = ccw, -1 = cw
from utils.viz import *


def sortByAng(start, p):
    if start[0] <= p[0]:
        return (p[1] - start [1])/length(start, p)
    else:
        return 2 - (p[1] - start [1])/length(start, p)

def merge(hullA, hullB):
    if len(hullA) == 2 == len(hullB) and orient(hullA[0], hullA[-1], hullB[0]) == 0 == orient(hullA[0], hullA[-1], hullB[-1]):
        return [hullA[0], hullB[-1]]
    n, m = len(hullA), len(hullB)
    #point furthest right from the left hull
    xRightA = -float('inf')
    xRightIdx = -1
    for i, p in enumerate(hullA):
        if p[0] > xRightA:
            xRightA = p[0]
            xRightIdx = i
    #point furthest left from the right hull
    xLeftB = float('inf')
    xLeftIdx = -1
    for i in range(m-1, -1, -1):
        p = hullB[i]
        if p[0] <= xLeftB:
            xLeftB = p[0]
            xLeftIdx = i
    #finding upper tangent
    idxUpA, idxUpB = xRightIdx, xLeftIdx
    flag = False

    while not flag:
        flag = True
        breaker = idxUpA
        while orient(hullB[idxUpB], hullA[idxUpA], hullA[(idxUpA + 1)%n]) <= 0:
            idxUpA = (idxUpA + 1)%n
            if idxUpA == breaker: break

        if orient(hullA[idxUpA], hullB[0], hullB[-1]) == 0:
            idxUpB = m-1
            break

        while orient(hullA[idxUpA], hullB[idxUpB], hullB[(m + idxUpB - 1)%m]) >= 0:
            idxUpB = (m + idxUpB - 1)%m
            flag = False

    #finding lower tangent
    idxLowA, idxLowB = xRightIdx, xLeftIdx
    flag = False

    while not flag:
        flag = True
        breaker = idxLowB #if orient(allpoints[0], allpoints[-1], hullB[idxLowB]) == 1  else (idxLowB + 1)%m


        while orient(hullA[idxLowA], hullB[idxLowB], hullB[(idxLowB + 1)%m]) <= 0:
            idxLowB = (idxLowB + 1)%m
            if (idxLowB + 1)%m == breaker: break

        if orient(hullB[idxLowB], hullA[0], hullA[-1]) == 0:
            idxLowA = 0
            break

        while orient(hullB[idxLowB], hullA[idxLowA], hullA[(n + idxLowA - 1)%n]) >= 0:
            idxLowA = (n + idxLowA - 1)%n
            flag = False


    #merging hulls together
    if hullA[idxLowA][1] <= hullB[idxLowB][1]:
        hull = [hullA[idxLowA], hullB[idxLowB]]
        while idxLowB != idxUpB:
            idxLowB = (idxLowB + 1)%m
            hull.append(hullB[idxLowB])
        while idxUpA != idxLowA:
            hull.append(hullA[idxUpA])
            idxUpA = (idxUpA+1)%n 
    else:
        hull = [hullB[idxLowB]]
        while idxLowB != idxUpB:
            idxLowB = (idxLowB + 1) % m
            hull.append(hullB[idxLowB])
        hull.append(hullA[idxUpA])
        while idxUpA != idxLowA:
            idxUpA = (idxUpA+1)%n 
            hull.append(hullA[idxUpA])

    return hull

def brute(points):
    n = len(points)
    hull = set()
    for i in range(n):
        for j in range(i+1,n):
            pos, neg = 0, 0
            for p in points:
                ori = orient(points[i], points[j], p)
                if ori > 0:
                    pos += 1
                elif ori < 0:
                    neg += 1
                else:
                    minX, minY = min(points[i][0], points[j][0]), min(points[i][1], points[j][1])
                    maxX, maxY = max(points[i][0], points[j][0]), max(points[i][1], points[j][1])
                    if minX <= p[0] <= maxX and minY <= p[1] <= maxY:
                        neg += 1
                        pos += 1
            if pos == n or neg == n:
                hull.add( (points[i][0], points[i][1]) )
                hull.add( (points[j][0], points[j][1]) )
    hull = list(hull)
    #sorting counterclockwise starting from the lowest point
    start, idx = (float('inf'), float('inf')), -1
    for i, p in enumerate(hull):
        if p[1] < start[1] or (p[1] == start[1] and p[0] < start[0]):
            start = p
            idx = i
    hull.pop(idx)
    hull.sort(key = lambda x: sortByAng(start, x))
    hull.insert(0, start)
    return hull

def recursive(points):
    n = len(points)
    if n < 8:
        hull = brute(points)
        return hull
    left = points[:n//2]
    right = points[n//2:]
    leftHull = recursive(left)
    rightHull = recursive(right)
    return merge(leftHull, rightHull)

def divideconquer(points):
    newpoints = sorted(points)
    hull = recursive(newpoints)
    return hull

### funcsVis ####

def mergeVis(hullA, hullB, ptsPlt, lnsPlt, lvl):
    if len(hullA) == 2 == len(hullB) and orient(hullA[0], hullA[-1], hullB[0]) == 0 == orient(hullA[0], hullA[-1], hullB[-1]):
        return [hullA[0], hullB[-1]]
    n, m = len(hullA), len(hullB)
    #point furthest right from the left hull
    xRightA = -float('inf')
    xRightIdx = -1
    for i, p in enumerate(hullA):
        if p[0] > xRightA:
            xRightA = p[0]
            xRightIdx = i
    #point furthest left from the right hull
    xLeftB = float('inf')
    xLeftIdx = -1
    for i in range(m-1, -1, -1):
        p = hullB[i]
        if p[0] <= xLeftB:
            xLeftB = p[0]
            xLeftIdx = i
    #finding upper tangent
    idxUpA, idxUpB = xRightIdx, xLeftIdx
    flag = False

    while not flag:
        flag = True
        breaker = idxUpA
        while orient(hullB[idxUpB], hullA[idxUpA], hullA[(idxUpA + 1)%n]) <= 0:
            idxUpA = (idxUpA + 1)%n
            if idxUpA == breaker: break

        if orient(hullA[idxUpA], hullB[0], hullB[-1]) == 0:
            idxUpB = m-1
            break

        while orient(hullA[idxUpA], hullB[idxUpB], hullB[(m + idxUpB - 1)%m]) >= 0:
            idxUpB = (m + idxUpB - 1)%m
            flag = False

    #finding lower tangent
    idxLowA, idxLowB = xRightIdx, xLeftIdx
    flag = False

    while not flag:
        flag = True
        breaker = idxLowB #if orient(allpoints[0], allpoints[-1], hullB[idxLowB]) == 1  else (idxLowB + 1)%m


        while orient(hullA[idxLowA], hullB[idxLowB], hullB[(idxLowB + 1)%m]) <= 0:
            idxLowB = (idxLowB + 1)%m
            if (idxLowB + 1)%m == breaker: break

        if orient(hullB[idxLowB], hullA[0], hullA[-1]) == 0:
            idxLowA = 0
            break

        while orient(hullB[idxLowB], hullA[idxLowA], hullA[(n + idxLowA - 1)%n]) >= 0:
            idxLowA = (n + idxLowA - 1)%n
            flag = False

    ptsPlt.append((lvl, PointsCollection(hullA, color='red')))
    ptsPlt.append((lvl, PointsCollection(hullB, color='blue')))
    lnsA = [[hullA[i-1], hullA[i]] for i in range(len(hullA))]
    lnsB = [[hullB[i-1], hullB[i]] for i in range(len(hullB))]
    lnsPlt.append( (lvl, LinesCollection(lnsA, color='black')) )
    lnsPlt.append( (lvl, LinesCollection(lnsB, color='black')) )
    lnsPlt.append( (lvl, LinesCollection([[hullA[idxUpA], hullB[idxUpB]]], color='yellow')) )
    lnsPlt.append( (lvl, LinesCollection([[hullA[idxLowA], hullB[idxLowB]]], color='green')) )
    #merging hulls together
    if hullA[idxLowA][1] <= hullB[idxLowB][1]:
        hull = [hullA[idxLowA], hullB[idxLowB]]
        while idxLowB != idxUpB:
            idxLowB = (idxLowB + 1)%m
            hull.append(hullB[idxLowB])
        while idxUpA != idxLowA:
            hull.append(hullA[idxUpA])
            idxUpA = (idxUpA+1)%n 
    else:
        hull = [hullB[idxLowB]]
        while idxLowB != idxUpB:
            idxLowB = (idxLowB + 1) % m
            hull.append(hullB[idxLowB])
        hull.append(hullA[idxUpA])
        while idxUpA != idxLowA:
            idxUpA = (idxUpA+1)%n 
            hull.append(hullA[idxUpA])

    return hull

def recursiveVis(points, ptsPlt, lnsPlt, lvl):
    n = len(points)
    if n < 8:
        hull = brute(points)
        ptsPlt.append((lvl+1, PointsCollection(hull, color='red')))
        lns = [[hull[i-1] , hull[i]] for i in range(len(hull)) ]
        lnsPlt.append((lvl+1, LinesCollection(lns, color='black')))
        return hull
    left = points[:n//2]
    right = points[n//2:]
    leftHull = recursiveVis(left, ptsPlt, lnsPlt, lvl + 1)
    rightHull = recursiveVis(right, ptsPlt, lnsPlt, lvl + 1)
    hull =  mergeVis(leftHull, rightHull, ptsPlt, lnsPlt, lvl + 1)
    ptsPlt.append((lvl+0.5, PointsCollection(hull, color='red')))
    lns = [[hull[i-1] , hull[i]] for i in range(len(hull)) ]
    lnsPlt.append((lvl+0.5, LinesCollection(lns, color='black')))
    return hull


def divideconquerVis(points):
    newpoints = sorted(points)
    ptsPlt = [(10**10, PointsCollection(points))]
    lnsPlt = [(10**10, LinesCollection([]))]
    hull = recursiveVis(newpoints, ptsPlt, lnsPlt, 0)
    ptsPlt = sorted(ptsPlt, key = lambda x: -x[0])
    lnsPlt = sorted(lnsPlt, key = lambda x: -x[0])
    scenes = []
    i, j = 0, 0
    n, m = len(ptsPlt), len(lnsPlt)
    pts, lns = [], []
    while i < n:
        temp= []
        k = i
        while k < n and ptsPlt[i][0] == ptsPlt[k][0]:
            temp.append(ptsPlt[k][1])
            k += 1
        i = k
        pts.append(temp)
    while j < m:
        temp = []
        k = j
        while k < m and lnsPlt[j][0] == lnsPlt[k][0]:
            temp.append(lnsPlt[k][1])
            k += 1
        j = k
        lns.append(temp)
    pts.append( [PointsCollection(hull, color = 'red')  ,PointsCollection(points, zorder =-1)] )
    lns.append( [LinesCollection([[hull[i-1] , hull[i]] for i in range(len(hull))], color='black' ) ] )
    scenes = [Scene( points= pts[i], lines = lns[i] ) for i in  range(len(pts))]
    return scenes
          