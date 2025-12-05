# note:
# simple enough but I wonder how my solution will affect part 2?
# OK LOL commiting this as it has a memory error, i see the issue
# will solve later

f = open("test.txt")
f = f.read().split("\n\n")

ranges = f[0].split("\n")
ingredients = f[1].split("\n")

avail = {}

for r in ranges:
    s, e = map(int, r.split("-"))
    avail.update({i: 1 for i in range(s, e + 1)})

c = 0
for i in ingredients:
    if int(i) in avail:
        c += 1

print(c)
