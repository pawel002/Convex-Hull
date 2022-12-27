import json

def saveList(points, filename):
    with open(filename, 'w') as outfile:
        for point in points:
            outfile.write(str(point[0]) + " " + str(point[1]) + "\n")


def readList(filename):
    with open(filename, 'r') as infile:
        lines = infile.readlines()
        arr = [[0, 0] for x in range(len(lines))]
        for i, line in enumerate(lines):
            line.replace('\n', '')
            x = line.split(' ')
            arr[i][0], arr[i][1] = float(x[0]), float(x[1])

        return arr
    
    
    