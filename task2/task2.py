import math

path1, path2 = input(), input()

with open(path1) as circle, open(path2) as dot:
    x, y, r = map(int, circle.read().split())
    dots = map(lambda s: tuple(map(int, s.split())), dot.read().split('\n'))
    for point in dots:
        point_x, point_y = point
        distance = math.sqrt((point_x - x) ** 2 + (point_y - y) ** 2)
        if distance < r:
            print(1)
        elif distance == r:
            print(0)
        else:
            print(2)
