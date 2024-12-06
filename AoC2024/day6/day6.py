with open("input.txt", "r") as f:
    data_parsed = f.read()
    
data_parsed = data_parsed.splitlines()
data = []
row = col = 0
for i in data_parsed:
    temp = []
    for char in i:
        temp.append(char)
        if char == '^':
            pos = [row, col]
        col += 1
    data.append(temp)
    row += 1
    col = 0

dir = [-1, 0]
visited = []
while 0 <= pos[0] <= len(data) and 0 <= pos[1] <= len(data[0]):
    if pos not in visited:
        visited.append([pos[0], pos[1]])
    #print(pos)
    try:
        if data[pos[0] + dir[0]][pos[1] + dir[1]] == '#':
            if dir == [-1, 0]:
                dir = [0, 1]
            elif dir == [0, 1]:
                dir = [1, 0]
            elif dir == [1, 0]:
                dir = [0, -1]
            elif dir == [0, -1]:
                dir = [-1, 0]
        pos[0] += dir[0]
        pos[1] += dir[1]
    except:
        break

print("part 1:", len(visited))