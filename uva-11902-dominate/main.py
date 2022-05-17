import sys

def dfs(adjList, u, visited, disableVertex = -1):
	if visited[u] == 1 or u == disableVertex:
		return
	
	visited[u] = 1

	for v in adjList[u]:
		dfs(adjList, v, visited, disableVertex)

def findDominates(adjList):
	nVertex = len(adjList)

	firstVisited = [0] * nVertex
	dfs(adjList, 0, firstVisited) #find reachable vertices when no disable vertex

	dominates = [[0]*nVertex for _ in range(nVertex)]

	for u in range(nVertex):
		secondVisited = [0] * nVertex
		dfs(adjList, 0, secondVisited, disableVertex = u)
		for v in range(nVertex):
			if firstVisited[v] == 1 and secondVisited[v] == 0: 	# disable u then v unreachable
				dominates[u][v] = 1								# so, u dominates v

	return dominates

def prettyPrint(dominates):
	n = len(dominates)
	delim = '+' + '-'*(2*n-1) + '+'
	print(delim)
	for u in range(n):
		print(end='|')
		for v in range(n):
			if dominates[u][v] == 1:
				print('Y', end='|')
			else:
				print('N', end='|')
		print()
		print(delim)

def readInput():
	nVertex = int(sys.stdin.readline())

	adjList = [[] for _ in range(nVertex)]

	for u in range(nVertex):
		arr = list(map(int, sys.stdin.readline().split()))
		for v, k in enumerate(arr):
			if k == 1:
				adjList[u].append(v)

	return adjList


def handleTc(id):
	adjList = readInput()
	dominates = findDominates(adjList)
	print('Case {}:'.format(id+1))
	prettyPrint(dominates)

# main
nTc = int(sys.stdin.readline())
for i in range(nTc):
	handleTc(i)


# python3 main.py < input