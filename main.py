import math
from unionfind import unionfind
import sys

# input
# 4 20  # n: n_city r: threshold
# 0 0   # location of city 0
# 40 30 # location of city 1
# 30 30 # ...
# 10 10


n,r = map(int, sys.stdin.readline().split())

positions = []
for _ in range(n):
    x,y = map(int, sys.stdin.readline().split())
    positions.append((x,y))

edgeList = []
for i in range(n):
    for j in range(i+1, n):
        xi,yi = positions[i]
        xj,yj = positions[j]
        w = int(math.sqrt((xi - xj) ** 2 + (yi - yj) ** 2))
        edgeList.append((i,j,w))

print(edgeList)

def weight(edge):
    return edge[2]

edgeList = sorted(edgeList, key=weight)

print(edgeList)

# kruskal
uf = unionfind(n)
road, rail, states = 0,0,1

for e in edgeList:
    u,v,w = e

    if uf.issame(u,v): # connect u,v form a cycle, so ignore
        print(u, v, w, 'form cycle')
        continue

    # connect (u,v) NOT form a cycle, so connect
    uf.unite(u,v)
    print(u, v, w, 'not form cycle')

    if w <= r: # u,v in the same state, so build road
        road += w
        print('road', road)
    else: # u,v in different state, so build rail
        rail += w
        states += 1
        print('rail', rail, 'states', states)

print(states, road, rail)


