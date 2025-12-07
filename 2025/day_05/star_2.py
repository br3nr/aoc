# note:
# first loop checking for overlaps of windows: o(n^2) worst case
# second loops adds up the window sizs.
# also the windows are sorted by the first value

# im on a plane to sydney with no wifi so cant test if
# this works (update: it worked)

f = open("input.txt")
ranges = f.read().split("\n\n")[0].split("\n")

vals = []
for r in ranges:
    l, h = map(int, r.split("-"))
    vals.append([l, h])

vals.sort(key=lambda x: x[0])

windows = []
for val in vals:
    if not windows:
        windows.append(val)
    else:
        overlap = False
        for win in windows:
            if val[0] >= win[0] and val[0] <= win[1]:
                overlap = True
                if val[1] >= win[1]:
                    win[1] = val[1]
                break
        if not overlap:
            windows.append(val)

c = 0
for win in windows:
    c += abs(win[1] - win[0]) + 1

print(c)
