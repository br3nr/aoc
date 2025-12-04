# note:
# this one seems really easy
# update: it was. At first I thought that it was gonna be one of
# those impossible to do brute force but I quickly realised it
# wouldnt be.
# I am pretty sure you can DFS this problem which I might come
# back to as a practice point.

f = open("input.txt")
f = f.read().split("\n")

grid = []
for line in f:
    grid.append(list(map(str, line)))

directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
n, m = len(grid), len(grid[0])
rolls = 0

updoot = []
while True:
    for y in range(n):
        for x in range(m):
            counter = 0
            if grid[y][x] != "@":
                continue

            for dy, dx in directions:
                ny, nx = y + dy, x + dx
                if 0 <= ny < n and 0 <= nx < m:
                    if grid[ny][nx] == "@":
                        counter += 1

            if counter < 4:
                rolls += 1
                updoot.append((y, x))

    if not updoot:
        break

    for y, x in updoot:
        grid[y][x] = "."

    updoot = []

print(rolls)
