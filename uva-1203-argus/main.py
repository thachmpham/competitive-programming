# https://www.udebug.com/UVa/1203

import sys, heapq

timeout = {} # id: time
a = []

while True:
    elems = sys.stdin.readline().split()

    if elems[0] == '#':
        break

    id, time = int(elems[1]), int(elems[2])
    timeout[id] = time
    heapq.heappush(a, (time, id))

n = int(sys.stdin.readline())

for _ in range(n):
    time, id = heapq.heappop(a)
    print(id)
    nextTime = time + timeout[id]
    heapq.heappush(a, (nextTime, id))
