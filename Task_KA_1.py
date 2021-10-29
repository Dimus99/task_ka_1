N = int(input())
num=0
inp=[]
while True:
    inp = inp + input().split()
    if inp[-1] == "32767":

        break
inp = [int(i) for i in inp]
matrix = [[] for i in range(inp[0]-2)]
m={i:{} for i in range(inp[0]-2)}
r=set()
for i in range(inp[0]-2):
    n = inp[i]-1
    nend=inp[i+1]-1
    for j in range(n,nend,2):
        m[i][inp[j]-1]=inp[j+1]
        r.add((i,inp[j]-1,inp[j+1]))
g=set()
res=set()
while len(g) < inp[0]-2:
    minimum = (0,0,9999999999)
    for v in r:
        if v[2]<minimum[2]:
            minimum=v
    if minimum[0] in g and minimum[1] in r:
        r.remove(minimum)
        continue
    res.add(minimum)
    g.add(minimum[0])
    g.add(minimum[1])
    r.remove(minimum)
for i in range(inp[0]-2):
    a=set()
    for v in res:
        if v[0] == i:

            if v[1] not in a:
                print(v[1]+1,end=" ")
            a.add(v[1])
        elif v[1]==i:
            if v[0] not in a:
                print(v[0]+1,end=" ")
            a.add(v[0])

    print()
print(sum([i[2] for i in res]))