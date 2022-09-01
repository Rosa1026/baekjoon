import sys

T = int(sys.stdin.readline())
s = []

for i in range(T):
    n = int(sys.stdin.readline())
    dp = []
    for j in range(2):
        dp.append(list(map(int, input().split())))
    for j in range(1, n):
        if j == 1:
            dp[0][j] += dp[1][j-1]
            dp[1][j] += dp[0][j-1]
        else:
            dp[0][j] += max(dp[1][j-1],dp[1][j-2])
            dp[1][j] += max(dp[0][j-1],dp[0][j-2])
    s.append(max(dp[0][n-1],dp[1][n-1]))

for i in range(0,T):
    print(s[i])