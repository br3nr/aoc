f = open("input.txt")
f = f.read().split("\n")

# Star 2: 
# Bad approach: try remove a single element from each bad version to see if it becomes good
#   - time complexity sucks
#
# Good approach: 

a = set(["1", "2"])

f = open("input.txt")
f = f.read().split("\n")

count = 0
reports = []

def check_safe(row):

    pset = set([1, 2, 3])
    nset = set([-1, -2, -3])

    for i in range(len(row)-1):
        diff = row[i] - row[i+1]
        pset.add(diff)
        nset.add(diff)
    print(pset, nset)
    return True if (len(pset) == 3 or len(nset) == 3) else False


for line in f:
    # I dont mind this solution but wonder if there is a cooler way to solve it

    l = line.split()
    l = list(map(int, l))

    print(check_safe(l))