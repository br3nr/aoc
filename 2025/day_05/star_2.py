# note: 
# simple enough but I wonder how my solution will affect part 2?


f = open("test.txt")
f = f.read().split("\n\n")

ranges = f[0].split("\n")

c = 0

vals = []
for r in ranges:
    l, h = map(int, r.split("-"))
    vals.append([l,h])

vals.sort(key=lambda x: x[0])
print(vals)


c = 0 
for i in range(len(vals) - 1):
    curr = vals[i]
    nxt = vals[i + 1]

    if curr[1] > nxt[0]:
        print("ye")
        vals[i+1][0] = curr[0]
        if curr[1] > nxt[1]:
            vals[i+1][1] = curr[1]
    else:
        print("no", curr[0], curr[1])
        c += abs(curr[1] - curr[0]) + 1

c += abs(vals[-1][1] - vals[-1][0]) + 1

print(vals)
print(c)
