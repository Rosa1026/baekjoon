import sys

N, M = map(int, sys.stdin.readline().split())
lst_arr = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
K = int(sys.stdin.readline())
dp = [[0 for _ in range(M+1)] for _ in range(N+1)]

for i in range(1, N+1):
    for j in range(1, M+1):
        dp[i][j] = lst_arr[i-1][j-1] + dp[i][j-1] + dp[i-1][j] - dp[i-1][j-1]

for _ in range(K):
    i, j, x, y = map(int, sys.stdin.readline().split())

    print(dp[x][y] - dp[x][j-1] - dp[i-1][y] + dp[i-1][j-1])