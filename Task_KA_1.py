def where(_dict, _value):
    r = set()
    for i in _dict.keys():
        if _value in _dict[i]:
            r.add(i)
    return r


file = open("input.txt")

N = int(file.readline())
num = 0
inp = []
while True:
    inp = inp + file.readline().split()
    if inp[-1] == "32767":
        break
inp = [int(i) for i in inp]
matrix = [[] for i in range(inp[0] - 2)]
m = {i: {} for i in range(inp[0] - 2)}
r = []
for i in range(inp[0] - 2):
    n = inp[i] - 1
    nend = inp[i + 1] - 1
    for j in range(n, nend, 2):
        m[i][inp[j] - 1] = inp[j + 1]
        r.append((min(i, inp[j] - 1), max(i, inp[j] - 1), inp[j + 1]))
r = list(set(r))
r.sort(key=lambda el: el[2])
link_r = 0
g = {i: {i} for i in range(len(matrix))}
res = set()
coo = len(matrix)
while coo > 1:
    minimum = (0, 0, 9999999999)
    while True:
        v = r[link_r]
        link_r += 1
        if not (where(g, minimum[0]) - where(g, minimum[1])):
            minimum = v
            break
    res.add(minimum)

    g[minimum[0]] = g[minimum[1]].union(g[minimum[0]])
    g[minimum[1]] = g[minimum[0]]
    coo -= 1
result = ""
for i in range(inp[0] - 2):
    a = set()
    for v in res:
        if v[0] == i:

            if v[1] not in a:
                result += str(v[1] + 1) + " "
            a.add(v[1])
        elif v[1] == i:
            if v[0] not in a:
                result += str(v[0] + 1) + " "
            a.add(v[0])

    result += "\n"
result += str(sum([i[2] for i in res]))
file.close()
file = open("output.txt", "w")
file.write(result)
file.close()
