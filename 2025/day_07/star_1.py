# note:
# tree time!
# first attempt was correct on the test set however I did not check
# if the next node was already visited, causing it to run for more
# than 10 seconds.
#
# second attempt was a matter of adding those checks and it was
# instant. I wonder how long it would have taken without these
# checks.

from collections import deque

f = open("input.txt").read()
f = list(map(str, f.split("\n")))

grid = []
for line in f:
    grid.append(list(map(str, line)))

r = c = 0
for i, c in enumerate(grid[0]):
    if c == "S":
        c = i
        break

queue = deque([(r, c)])
visited = {(r, c)}

directions = [(0, -1), (0, 1)]

n, m = len(grid), len(grid[0])

while queue:
    row, col = queue.popleft()
    if grid[row][col] == "^":
        if col - 1 >= 0:
            left = (row, col - 1)
            if left not in visited:
                queue.append(left)
                visited.add(left)
        if col + 1 < m:
            right = (row, col + 1)
            if right not in visited:
                queue.append(right)
                visited.add(right)
    else:
        below = (row + 1, col)
        if below[0] < n:
            if below not in visited:
                queue.append(below)
                visited.add(below)

manifolds = 0
for r, c in visited:
    if grid[r][c] == "^":
        manifolds += 1

print(manifolds)
