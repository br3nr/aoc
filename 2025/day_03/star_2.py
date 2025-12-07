# notes:
# solved this one on day 7, took me ages even tho I conceptually
# understood it. I just couldnt quite get the window sliding
# down.

# (つ╥﹏╥)つ i am glad this one is over

batteries = open("input.txt").read().split("\n")
c = 0
for bank in batteries:

    bank = list(map(int, bank))

    ptr = 0
    joltige = []
    dist = 12

    while len(joltige) != 12:
        dist = len(bank) - (12 - len(joltige)) + 1

        if ptr == dist:
            joltige.extend(bank[ptr:])
            break

        max_num = 0
        max_idx = ptr

        for i in range(ptr, dist):
            if bank[i] > max_num:
                max_num = bank[i]
                max_idx = i

        joltige.append(max_num)
        ptr = max_idx + 1

    c += int("".join(map(str, joltige)))

print(c)
