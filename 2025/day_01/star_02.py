# thinking
#
# ok so my thinking so far is that we know if a click happened
# as a product of the size of the number after the rotation.
#
# however, a number could click multiple times, so that wont work.
# maybe we can calculate how many ticks it would cause by itself?


import math

f = open("input.txt")
f = f.read().split("\n")

num = 50
count = 0

f = ["L68", "L30", "R48", "L5", "R60", "L55", "L1", "L99", "R14", "L82"]

print(num)
for turn in f:
    direction, rotations = turn[0], int(turn[1:])
    prev = num
    magnitute = rotations // 100
    if direction == "L":
        num = (num - rotations) % 100
        if num > prev and prev != 0:
            print(num, " clicked")
            count += 1
        else:
            print(num)
    else:
        num = (num + rotations) % 100
        if num < prev and prev != 0:
            print(num, " clicked")
            count += 1
        else:
            print(num)

    prev = num
    if num == 0:
        count += 1

print("Answer:")
print(count)
