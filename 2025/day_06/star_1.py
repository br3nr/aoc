# note:
# part 1 seems fine althought the input reading is a bit annoying
# I shall do regex, as a reason to read about it

import re
import math

f = open("input.txt")
f = f.read().split("\n")

homework = []
for l in f:
    print(l)
    homework.append(re.sub(r"\s+", " ", l.strip()).split(" "))

homework = list(zip(*homework))

c = 0
for p in homework:
    op = p[-1]
    nums = map(int, p[:-1])
    if op == "*":
        c += math.prod(nums)
    else:
        c += sum(nums)

print(c)