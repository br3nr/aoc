import re

f = open("input.txt")
f = f.read().split("\n")

sum = 0
for line in f:

    pattern = r"mul\((\d+),(\d+)\)"
    matches = re.findall(pattern, line, re.IGNORECASE)

    for match in matches:
        sum += int(match[0]) * int(match[1])

print(sum)
