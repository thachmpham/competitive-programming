import sys
import collections

def compute(R, C, M, N, waters):
    ans = [0,0]

    Q = collections.deque()
    visited = [[0]*C for _ in range(R)]

    Q.appendleft((0,0))
    visited[0][0] = 1

    dirs = [(-M, -N), (-M, N), (M, -N), (M, N),
        (-N, -M), (-N, M), (N, -M), (N, M)]
    
    # remove duplicated directions when:
    # M = 0 or N = 0
    # M = N
    dirs = list(set(dirs))

    while Q:
        r,c = Q.pop()
        count = 0

        # for neighbors of (r,c)
        for dr, dc in dirs:
            newR, newC = r+dr, c+dc
            if newR < 0 or newC < 0 or newR >= R or newC >= C:                
                continue

            if (newR, newC) in waters:
                continue
            
            count += 1

            # add neighbor to Q
            if visited[newR][newC] == 0:
                Q.appendleft((newR, newC))
                visited[newR][newC] = 1

        ans[count%2] += 1
    
    return ans



def handleTc(tc):
    R, C, M, N = list(map(int, sys.stdin.readline().strip().split()))
    W = int(sys.stdin.readline())
    
    waters = set()
    
    for _ in range(W):
        i,j = list(map(int, sys.stdin.readline().strip().split()))
        waters.add((i,j))
    
    odd,even = compute(R, C, M, N , waters)

    print('Case {}: {} {}'.format(tc+1, odd, even))

nTc = int(sys.stdin.readline())

for tc in range(nTc):
    handleTc(tc)
