def where(v1, v2, ng):
    for i in ng:
        if v1 in i and v2 in i:
            return False
        if v1 in i or v2 in i:
            return True
    return True


file = open("in.txt")

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
ng = [{i} for i in range(len(matrix))]
res = set()
coo = len(matrix)
while coo > 1:
    minimum = (0, 0, 9999999999)
    while True:
        v = r[link_r]
        link_r += 1

        if where(v[0], v[1], ng):
            minimum = v
            break
    res.add(minimum)
    nss = set()
    q=[]
    for ss in ng:
        if minimum[0] in ss or minimum[1] in ss:
            nss=nss.union(ss)
            q.append(ss)
    for ee in q:
        ng.remove(ee)
    ng.append(nss)
    g[minimum[0]] = g[minimum[1]].union(g[minimum[0]])
    g[minimum[1]] = g[minimum[0]]
    coo -= 1
result = ""
for i in range(inp[0] - 2):
    a = set()
    res1 = []
    for v in res:
        rr = []
        if v[0] == i:

            if v[1] not in a:
                res1.append(str(v[1] + 1))
            a.add(v[1])
        elif v[1] == i:
            if v[0] not in a:
                res1.append(str(v[0] + 1))
            a.add(v[0])
    result += " ".join(sorted(res1))

    result += " 0\n"
result += str(sum([i[2] for i in res]))
file.close()
file = open("out.txt", "w")
file.write(result)
file.close()
