import sys

def toInt(c):
    return ord(c) - ord('A')


def handleInput():
    V = toInt(sys.stdin.readline().strip()) + 1
    
    adjList = [[] for _ in range(V)]

    while True:
        s = sys.stdin.readline().strip()        
        if not s:
            break
        u, v = toInt(s[0]), toInt(s[1])
        adjList[u].append(v)
        adjList[v].append(u)
    
    return adjList


def dfs(adjList, u, visited):
    if visited[u]:
        return
    
    visited[u] = 1

    for v in adjList[u]:
        if not visited[v]:
            dfs(adjList, v, visited)

def findNumComp(adjList):
    V = len(adjList)
    visited = [0] * V
    
    numComp = 0

    for u in range(V):
        if not visited[u]:
            numComp += 1
            dfs(adjList, u, visited)

    return numComp

# main
nTc = int(sys.stdin.readline())
sys.stdin.readline()

for i in range(nTc):
    adjList = handleInput()
    n = findNumComp(adjList)
    print(n)
    if i < nTc-1:
        print()