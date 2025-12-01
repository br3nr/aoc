file = open("input.txt")
grid = [list(line.strip()) for line in file]

xmas_count = 0
for r in range(len(grid)):
    for c in range(len(grid[r])):
        if grid[r][c] != "A": continue
        if r - 1 < 0 or r + 1 >= len(grid) or c - 1 < 0 or c + 1 >= len(grid[r]): continue

        xmas_dict = {}        
        xmas_str = f"{grid[r-1][c-1]}{grid[r-1][c+1]}{grid[r+1][c-1]}{grid[r+1][c+1]}"

        if xmas_str in ["SSMM", "MMSS", "MSMS", "SMSM"]:
            xmas_count+=1

print(xmas_count)