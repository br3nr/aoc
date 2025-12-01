file = open("input.txt")
grid = [list(line.strip()) for line in file]

xmas_count = 0
for r in range(len(grid)):
    for c in range(len(grid[r])):
        
        if grid[r][c] != "X": continue
        for dr in [-1, 0, 1]:
            for dc in [-1, 0, 1]:
                if not (0 <= r + 3 * dr < len(grid) and 0 <= c + 3 * dc < len(grid[0])): continue
                if grid[r + 3*dr][c + 3*dc] == "S" and grid[r+ 2*dr][c+ 2*dc] == "A" and grid[r+ dr][c + dc] == "M":
                    xmas_count += 1

print(xmas_count)