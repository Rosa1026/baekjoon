import sys

N, M = [int(x) for x in sys.stdin.readline().split()]

A = list(map(int, input().split()))
B = list(map(int, input().split()))
c = sorted(A+B)

for i in range(N+M):
    print(c[i], end=' ')