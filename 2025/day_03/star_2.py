# notes:
# hahaha
# oh god, ok
# this is a bit cooked.

# ok so the gaps can be distributed all along the battery
# 234234234234278 is 434234234278
#   ^ ^^^^^^^^^^^
# 91919191919191919191919191 would have a final number of 999999999999
# perhaps, we can rotate the highest values down, like shuffle down
# or shuffle up?

# if we get to a certain number of values, we would know that all subsequent ones are added to the sequence

f = open("input.txt")
batteries = f.read().split("\n")

batteries = ["234234234234278"]

counter = 0
for bank in batteries:
    low, high = 0, 0
    print(len(bank))
    bank = list(map(int, bank))

