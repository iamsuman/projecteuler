#!/usr/bin/python


def dist(p1, p2):
    (x1,y1) = p1
    (x2, y2) = p2
    distance = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** .5
    return distance


def dist_points(points):
    no_points = points.__len__()
    if no_points <= 1:
        print("Need min 2 points to get distance")
        exit(1)

    _min = None

    _output = []

    for i in range(0, no_points):
        for j in range(i, no_points):
            if i == j: continue
            _dist = dist(points[i], points[j])
            if _min == None:
                _min = _dist
            else:
                if _dist < _min: _min = _dist
            _output.append([points[i], points[j], _dist])
    return _min, _output


def main():
    print("Please Enter List of points to be verified: ")
    points = input()

    _min, distpoints = dist_points(points)

    print("Points with Shortest distance")
    for i in distpoints:
        if i[2] == _min:
            print(i)


if __name__ == '__main__':
    main()





