# this at first seemed complicated until I realised
# that 1011 is not a silly number due to double 1's.
# But 1010 is silly, which is just a matter of halving
# the number.

f = open("input.txt")
f = f.read().split(",")

count = 0
for ranges in f:

    print(f"Range: {ranges}")
    start, end = map(int, ranges.split("-"))

    for i in range(start, end + 1):
        istr = str(i)
        mid = len(istr) // 2
        if istr[:mid] == istr[mid:]:
            print(f"Silly number found: {i}")
            count += i

print(count)
