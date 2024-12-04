with open("input.txt", "r") as f:
    data = f.read()

data2 = data.splitlines()
rows = len(data2)
cols = len(data2[0])
grid = [[data2[row][col] for col in range(cols)] for row in range(rows)]

cnt = 0
for row in range(rows):
    for col in range(cols - 3):
        if grid[row][col] == "X" and grid[row][col + 1] == "M" and grid[row][col + 2] == "A" and grid[row][col + 3] == "S":
            cnt += 1
for row in range(rows):
    for col in range(3, cols):
        if grid[row][col] == "X" and grid[row][col - 1] == "M" and grid[row][col - 2] == "A" and grid[row][col - 3] == "S":
            cnt += 1
for row in range(rows - 3):
    for col in range(cols):
        if grid[row][col] == "X" and grid[row + 1][col] == "M" and grid[row + 2][col] == "A" and grid[row + 3][col] == "S":
            cnt += 1
for row in range(3, rows):
    for col in range(cols):
        if grid[row][col] == "X" and grid[row - 1][col] == "M" and grid[row - 2][col] == "A" and grid[row - 3][col] == "S":
            cnt += 1
for row in range(rows - 3):
    for col in range(cols - 3):
        if grid[row][col] == "X" and grid[row + 1][col + 1] == "M" and grid[row + 2][col + 2] == "A" and grid[row + 3][col + 3] == "S":
            cnt += 1
for row in range(3, rows):
    for col in range(3, cols):
        if grid[row][col] == "X" and grid[row - 1][col - 1] == "M" and grid[row - 2][col - 2] == "A" and grid[row - 3][col - 3] == "S":
            cnt += 1
for row in range(rows - 3):
    for col in range(3, cols):
        if grid[row][col] == "X" and grid[row + 1][col - 1] == "M" and grid[row + 2][col - 2] == "A" and grid[row + 3][col - 3] == "S":
            cnt += 1
for row in range(3, rows):
    for col in range(cols - 3):
        if grid[row][col] == "X" and grid[row - 1][col + 1] == "M" and grid[row - 2][col + 2] == "A" and grid[row - 3][col + 3] == "S":
            cnt += 1

print("part 1:", cnt)
cnt = 0

def checkXMAS(row, col):
    try:
        aa = grid[row - 1][col - 1] + grid[row + 1][col + 1]
        bb = grid[row - 1][col + 1] + grid[row + 1][col - 1]
        if grid[row][col] == "A" and {aa, bb}.issubset({"MS", "SM"}):
            return 1
    except IndexError:
        return 0
    return 0

for row in range(1, rows - 1):
    for col in range(1, cols - 1):
        cnt += checkXMAS(row, col)

print("part 2:", cnt)