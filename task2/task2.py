import math
import argparse
parser = argparse.ArgumentParser()
parser.add_argument("circle_path")
parser.add_argument("dots_path")
args = parser.parse_args()

path1, path2 = args.circle_path, args.dots_path

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
