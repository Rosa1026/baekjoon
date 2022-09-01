import sys

N = int(sys.stdin.readline())
num = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

k = 2
for i in range(1, N):
    for j in range(k):
        if j == 0:
            num[i][j] = num[i][j] + num[i-1][j]
        elif i == j:
            num[i][j] = num[i][j] + num[i-1][j-1]
        else:
            num[i][j] = num[i][j] + max(num[i-1][j-1], num[i-1][j])
    k += 1

print(max(num[N-1]))