# notes:
# i am feeling that this one, we track the low number. When we encounter a new high, we update the
# highest low and then reset high, as it assumes that a new highest low will be higher than all prevs.
#
# update from finished solution, yes that is correct and was pretty simple.
# i think its important to not go straight to algo concepts. thinking of the problem
# as a sliding window or two pointer made me get to this a bit slower.
# hope part two is ok (probably not)

f = open("input.txt")
batteries = f.read().split("\n")

counter = 0
for bank in batteries:
    low, high = 0, 0
    bank = list(map(int, bank))
    for i in range(len(bank) - 1):
        if bank[i] > low:
            high = 0
            low = bank[i]
        if bank[i + 1] > high:
            high = bank[i + 1]

    counter += low * 10 + high

print(counter)
