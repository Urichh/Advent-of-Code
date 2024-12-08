with open("input.txt") as f:
    data = f.read()

ants = []
lines = data.strip().split("\n")
w = len(lines[0])
h = len(lines)

for y, line in enumerate(lines):
    for x, char in enumerate(line):
        if char != '.':
            ants.append((x, y, char))

antiants = set()
freq = {}

for x, y, i in ants:
    if i not in freq:
        freq[i] = []
    freq[i].append((x, y))

for freq, pos in freq.items():
    n = len(pos)
    for i in range(n):
        for j in range(i + 1, n):
            x1, y1 = pos[i]
            x2, y2 = pos[j]
            dx = x2 - x1
            dy = y2 - y1
            ax1 = x1 - dx
            ay1 = y1 - dy
            ax2 = x2 + dx
            ay2 = y2 + dy

            if 0 <= ax1 < w and 0 <= ay1 < h:
                antiants.add((ax1, ay1))
            if 0 <= ax2 < w and 0 <= ay2 < h:
                antiants.add((ax2, ay2))

res = len(antiants)
print("part 1:", res)
