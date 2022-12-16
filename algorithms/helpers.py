from math import sqrt

eps = 10**(-10)

def det(a, b, c):
    return (a[0] - c[0])*(b[1] - c[1]) - (b[0] - c[0])*(a[1] - c[1])

def orient(a, b, c):
    d = det(a, b, c)
    if d > eps:
        return 1
    elif d < eps:
        return -1
    return 0
    
def lengthSquared(a, b):
    return (a[0] - b[0])*(a[0] - b[0]) + (a[1] - b[1])*(a[1] - b[1])

def length(a, b):
    return sqrt(lengthSquared(a, b))

