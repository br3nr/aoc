f = open("input.txt")
f = f.read().split("\n")

count = 0
reports = []
for line in f:
    # I dont mind this solution but wonder if there is a cooler way to solve it

    l = line.split()
    l = list(map(int, l))
    safe = True
    dir = ""
    
    for i in range(len(l)-1):      
        diff = l[i] - l[i+1]
        if i == 0:
            # Note down if we are going positive or negative
            dir = "P" if diff > 0 else "N"
        else:
            # if we encounter a different direction its not safe
            dir_tmp = "P" if dir > 0 else "N"
            if dir_tmp != dir:
                safe = False

        if abs(diff) > 3:
            # if the difference is greater than 3 its not safe
            safe = False
        if l[i] == l[i+1]:
            # if they are consecutive its not safe
            safe = False

    if safe == True:
        count += 1

print(count)
