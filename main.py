import heapq
from heapq import heappush, heappop
import sys

'''
how to go from 1 to 7:
1 3 6 7: max weight edge: maxWeight1 = 140      
1 2 4 7: max weight edge: maxWeight2 = 120   
1 2 5 7: max weight edge: maxWeight3 = 90
1 2 4 6 7: max weight edge: maxWeight4 = 120 
1 3 6 4 7: max weight edge: maxWeight5 = 80

min of [maxWeight1...maxWeight5] = 80
-> call that: minimax(1,7) = 80

how to solve:
use Prim algorithm

expand tree from 1,
each step choose the smallest edge next to the tree
    trace the maxWeight each expanding step
repeat until reach 7


'''

nV, nE, nQ = map(int, sys.stdin.readline().split())

adjList = [[] for _ in range(nV+1)]

for _ in range(nE):
    u,v,w = map(int, sys.stdin.readline().split())
    adjList[u].append((v,w))
    adjList[v].append((u,w))


# greedily expands MST from s to t
# each step, expand the smallest edge
def prim(s, t):
    mst = set()
    opens = []
    heapq.heappush(opens, (0,s)) # push((weight, vertex))

    maxWeight= 0

    while opens:
        weight,u = heapq.heappop(opens)

        if u in mst:
            continue

        print(u, weight)
        maxWeight = max(maxWeight, weight)

        if u == t:
            print(maxWeight)
            break

        mst.add(u)

        for v,w in adjList[u]:
            if v in mst:
                continue

            heapq.heappush(opens, (w,v))

# find mimimax weight of paths from 1 to 7
prim(1,7)

# prim(2,6)