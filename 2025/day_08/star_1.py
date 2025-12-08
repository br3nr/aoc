# note:
# is o(n^2) innevitable? 


import math

# 162,817,812

f = open("test.txt")
f = f.read().split("\n")


coords = []
for line in f:
    coords.append(tuple(map(int, line.strip().split(','))))


distances = []
for i, c1 in enumerate(coords):
    for j, c2 in enumerate(coords):
        if i < j:
            d = math.dist(c1, c2)
            distances.append((d, c1, c2))

print(coords)
print(distances)
