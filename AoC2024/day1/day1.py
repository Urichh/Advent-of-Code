f = open("input.txt", "r")
vse = f.read()
vse = vse.split()
col1 = []
col2 = []
for i in range(0, len(vse)):
    if i % 2 == 0:
        col1.append(int(vse[i]))
    else:
        col2.append(int(vse[i]))

col1.sort()
col2.sort()

total = 0
similarity_score = 0
cnt = 0
for i in range(0, len(col1)):
    total += abs(col1[i] - col2[i])
    for n in range(0, len(col2)):
        if(col1[i] == col2[n]):
            cnt += 1
    similarity_score += col1[i] * cnt
    cnt = 0

print("part 1:", total)
print("part 2:", similarity_score)