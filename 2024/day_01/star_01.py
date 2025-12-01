f = open("input.txt")
f = f.read().split("\n")

a1, a2 = [], []
for l in f:
    s = l.split("   ")
    a1.append(int(s[0]))
    a2.append(int(s[1]))

a1.sort()
a2.sort()

d = 0
for i in range(len(a1)):
    d += abs(a1[i] - a2[i])

print(d)