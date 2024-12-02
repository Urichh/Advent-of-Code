def check(input):
    isRising = True
    isFalling = True

    for i in range(1, len(input)):
        wtf = input[i] - input[i - 1]

        if abs(wtf) < 1 or abs(wtf) > 3:
            return False

        if wtf > 0:
            isFalling = False
        elif wtf < 0:
            isRising = False

        if not isRising and not isFalling:
            return False
        
    return True

with open("input.txt", "r") as f:
    data_str = f.read().splitlines()

data = [list(map(int, row.split())) for row in data_str]
cnt = 0
for input in data:
    if check(input):
        cnt += 1
    else:
        for i in range(len(input)):
            input2 = input[:i] + input[i+1:]
            if check(input2):
                cnt += 1
                break

print(cnt)
