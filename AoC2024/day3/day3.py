import re

with open("input.txt", "r") as f:
    data = f.read()

matches = re.findall(r"mul\([0-9]{1,3},[0-9]{1,3}\)", data)

total = 0
for match in matches:
    print(match)
    left, right = match.split(',')
    print("left:", left, "right:", right)
    left = int(re.findall("[0-9]{1,3}", left)[0])
    right = int(re.findall("[0-9]{1,3}", right)[0])
    print("EXTRACTED: left:", left, "right:", right)
    total += left * right

print("part 1:", total)

matches = re.findall(r"(mul\([0-9]{1,3},[0-9]{1,3}\)|do\(\)|don't\(\))", data)

total = 0
isEnabled = True
for match in matches:
    if match == "do()":
        isEnabled = True
        continue
    elif match == "don't()":
        isEnabled = False
        continue
    else:
        if isEnabled == False:
            continue
        else:
            left, right = match.split(',')
            print("left:", left, "right:", right)
            left = int(re.findall("[0-9]{1,3}", left)[0])
            right = int(re.findall("[0-9]{1,3}", right)[0])
            print("EXTRACTED: left:", left, "right:", right)
            total += left * right

print("part 2:", total)