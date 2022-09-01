import sys

N = int(sys.stdin.readline())

dp = [[0]*10 for i in range(1001)]

for i in range(10):
    dp[1][i] = 1

for i in range(2, 1001):
    for j in range(10):
        for k in range(j+1):
            dp[i][j] += dp[i-1][k]

print(sum(dp[N])%10007, end='')