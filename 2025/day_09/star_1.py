f = open("input.txt").read()
f = f.split("\n")

print(f)
points = [list(map(int, point.split(","))) for point in f]

max = 0

for p1 in points:
    for p2 in points:
        if p1 is p2:
            continue

        w = abs(p2[0] - p1[0]) + 1
        h = abs(p2[1] - p1[1]) + 1
        area = w * h
        if area > max:
            max = area

print(max)
        
