# ok!
# this was one easy, is it optimal? probably not but i do not care.
# it takes around 2-3 seconds to run.
# the way I did this was to iterate through divisible numbers only
# and check if they are made up of repeating numbers.

# TODO: document optimal solutions

f = open("input.txt")
f = f.read().split(",")

count = 0
for ranges in f:
    start, end = map(int, ranges.split("-"))
    for i in range(start, end + 1):
        s = str(i)
        l = len(s)
        for j in range(1, l // 2 + 1):
            if l % j == 0:  # if its not divisible skip
                block = s[:j]
                times = l // j
                if block * times == s:  # multiply the string B)
                    count += i
                    break

print(count)
