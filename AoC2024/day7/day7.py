from itertools import product

with open("input.txt") as f:
    data_parsed = f.read().splitlines()

data = []
for line in data_parsed:
    temp = line.split(": ")
    temp2 = temp[1].split()
    data.append([int(temp[0]), [int(i) for i in temp2]])

res = 0
for bulica, nrs in data:
    combs = product("+*|", repeat=len(nrs) - 1)
    con = False

    for ops in combs:
        res = nrs[0]
        for i, op in enumerate(ops):
            if op == "+":
                res += nrs[i + 1]
            elif op == "*":
                res *= nrs[i + 1]
            elif op == "|":
                res = int(str(res) + str(nrs[i+1]))

        if res == bulica:
            res += bulica
            con = True
            break

    if con:
        continue

print("part 2:", res)
