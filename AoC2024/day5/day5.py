from collections import defaultdict, deque

with open("input.txt", "r") as f:
    data = f.read()

rules_parsed, pages_parsed = data.split("\n\n")
rules_parsed = rules_parsed.split()
rules = []
for rule in rules_parsed:
    temp = rule.split("|")
    temp2 = []
    for i in temp:
        temp2.append(int(i))
    rules.append(temp2)

pages_parsed = pages_parsed.split()
pages = []
for page in pages_parsed:
    temp = page.split(",")
    temp2 = []
    for i in temp:
        temp2.append(int(i))
    pages.append(temp2)

#print(rules)
cnt = 0
con = True
temp_nr = []
incorr = []
for page in pages:
    con = True
    temp_nr = []
    for nr in page:
        for i in rules:
            if i[1] == nr and i[0] in page and i[0] not in temp_nr:
                con = False
                break
        temp_nr.append(nr)
    if con:
        print(page)
        cnt += page[len(page)//2]
    else:
        incorr.append(page)

print("part 1:", cnt)

cnt = 0
def uredi(page, rules):
    graph = defaultdict(list)
    in_degree = defaultdict(int)

    for x, y in rules:
        if x in page and y in page:
            graph[x].append(y)
            in_degree[y] += 1
            if x not in in_degree:
                in_degree[x] = 0

    queue = deque([node for node in page if in_degree[node] == 0])
    sorted = []

    while queue:
        current = queue.popleft()
        sorted.append(current)
        for neighbor in graph[current]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    return sorted

for page in incorr:
    corr_page = uredi(page, rules)
    cnt += corr_page[len(corr_page)//2]

print("part 2:", cnt)