# note:
# yeyeyeyeyeye 
f = open("input.txt")
f = f.read().split("\n\n")

ranges = f[0].split("\n")
ingredients = map(int, f[1].split("\n"))

c = 0
for i in ingredients:
        for r in ranges:
            s, e = map(int, r.split("-"))
            if int(i) >= int(s) and int(i) <= int(e):
                c += 1
                break

print(c)
