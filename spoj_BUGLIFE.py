import sys, collections

# sys.stdin = open('input.txt', 'r')


'''
vertex: bug
edge:   bug-bug relation

bug genders:    male/female
vertex colors:  0/1

suspicious if there 2 bugs:
    - x relate to y
    &
    - x same gender as y
    
ok if for every bug x,y:
    - x related to y
    ->
    - x color different from y color

ok if every bug (x,y) in G, x.gender != y.gender
ok if every vertex (x,y) in G, x.color != y.color
'''

nTc = int(sys.stdin.readline())

def handleTc(tc):
    V, E = map(int, sys.stdin.readline().split())
    V += 1
    adjList = [[] for _ in range(V)]
    for _ in range(E):
        x, y = map(int, sys.stdin.readline().split())
        adjList[x].append(y)
        adjList[y].append(x)

    colors = [-1] * V

    def bicolor(x):
        Q = collections.deque()

        Q.append(x)
        colors[x] = 0

        while Q:
            x = Q.popleft()

            for y in adjList[x]:
                if colors[y] == -1:
                    colors[y] = 1 - colors[x]
                    Q.append(y)
                elif colors[y] == colors[x]:
                    return 0 # not bicolor, there suspicous bugs

        return 1

    print('Scenario #{}:'.format(tc))
    for x in range(1, V):
        if colors[x] == -1:
            bi = bicolor(x)
            if not bi:
                print('Suspicious bugs found!')
                return
    print('No suspicious bugs found!')

for tc in range(1, nTc+1):
    handleTc(tc)