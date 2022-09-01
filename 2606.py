import sys
from collections import deque

N = int(sys.stdin.readline())
n = int(sys.stdin.readline())
network = [[0]*(N+1) for _ in range(N+1)]

for _ in range(n):
    m1, m2 = map(int, sys.stdin.readline().split())
    network[m1][m2] = network[m2][m1] = 1

def BFS(a):
    cnt = 0
    pa = [a]
    queue = deque()
    queue.append(a)

    while queue:
        v = queue.popleft()

        for w in range(len(network[a])):
            if network[v][w] == 1 and (w not in pa):
                cnt += 1
                pa.append(w)
                queue.append(w)

    return cnt

print(BFS(1))