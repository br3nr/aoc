# note:
# This seems straightforward, need to undust my
# matrix traversal approach.

f = open("input.txt")
f = f.read().split("\n")

grid = []
for line in f:
    grid.append(list(map(str, line)))

directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
n, m = len(grid), len(grid[0])
rolls = 0

for y in range(n):
    for x in range(m):
        counter = 0
        if grid[x][y] != "@":
            continue

        for dy, dx in directions:
            ny, nx = y + dy, x + dx
            if 0 <= ny < n and 0 <= nx < m:
                if grid[ny][nx] == "@":
                    counter += 1

        if counter < 4:
            rolls += 1

print(rolls)
