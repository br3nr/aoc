f = open("input.txt")
f = f.read().split("\n")

a1, a2 = [], []
for l in f:
    s = l.split("   ")
    a1.append(int(s[0]))
    a2.append(int(s[1]))

a2_d = {}

for num in a2:
    a2_d[num] = a2_d.get(num, 0) + 1
    
sim_score = 0

for num in a1:
    if num in a2_d:
        sim_score += num * a2_d[num]


print(sim_score)