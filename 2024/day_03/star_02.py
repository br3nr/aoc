import re

f = open("input.txt")
f = f.read().split("do()")
sum = 0

# split based on each do()
for line in f:
    # now, split on don't(). We know all do() will fall at element 0
    line = line.split("don't()")[0]
    pattern = r"mul\((\d+),(\d+)\)"
    matches = re.findall(pattern, line, re.IGNORECASE)

    for match in matches:
        sum += int(match[0]) * int(match[1])

print(sum)
