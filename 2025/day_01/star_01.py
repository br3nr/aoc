f = open("input.txt")
f = f.read().split("\n")

num = 50
count = 0

for turn in f:
    direction, rotations = turn[0], int(turn[1:])

    if direction == "L":
        num = (num - rotations) % 100
    else:
        num = (num + rotations) % 100

    if num == 0:
        count += 1

print(count)
