import sys

N, M = map(int, sys.stdin.readline().split())
list_1 = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
M, K = map(int, sys.stdin.readline().split())
list_2 = [list(map(int, sys.stdin.readline().split())) for _ in range(M)]
list_a = [[0 for _ in range(K)] for _ in range(N)]

for i in range(N):
    for j in range(K):
        for k in range(M):
            list_a[i][j] += list_1[i][k]*list_2[k][j]

for i in list_a:
    for j in i:
        print(j, end=' ')
    print()