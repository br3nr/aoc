# Note:
# This one was really tricky, more than I expected.
# The hardest thing I had was getting enough edge cases to know where the solution was failing.
# If I had the full list below I would have found the solution faster.
# Another issue I had was trying to calculate the half and full spins in one go
# whereas ultimately all I had to do was break it down into smaller steps.
# If I drew this out and spent more time thinking about the problem I would have solved it faster.

# Test cases:
# f = ["L68", "L30", "R48", "L5", "R60", "L55", "L1", "L99", "R14", "L82", "R1000"]
# f = ["L50", "R50", "L50", "L50", "R50", "L50", "R50", "R50"]
# f = ["L150", "L50", "L150", "R50", "R150", "L50", "R150", "R50"]
# f = ["L500"]
# f = ["L5"]
# f = ["L5"]
# f = ["L150"]

f = open("input.txt")
f = f.read().split("\n")

start = 50
count = 0

for turn in f:
    if not turn:
        continue
    direction, rotations = turn[0], int(turn[1:])

    if direction == "L":
        end = (start - rotations) % 100
        spins = rotations // 100
        half_spin = end > start if start != 0 else False
    else:
        end = (start + rotations) % 100
        spins = rotations // 100
        half_spin = start > end if end != 0 else False

    if end == 0:
        count += 1

    if half_spin:
        count += 1

    count += spins
    start = end

print(count)
