import sys

N = int(sys.stdin.readline())
lst = [0] + list(map(int, sys.stdin.readline().split()))
cost = [0 for _ in range(N+1)]

cost[1] = lst[1]
for i in range(2, N+1):
    for j in range(1, i+1):
        if cost[i] < cost[i-j] + lst[j]:
            cost[i] = cost[i-j]+lst[j]

print(cost[N])