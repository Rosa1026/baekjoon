import sys

N = int(sys.stdin.readline())

dp = [[0]*11 for i in range(101)]

summ = 0

for i in range(1, 10):
    dp[1][i] = 1

for j in range(2,N+1):
    dp[j][0] = dp[j-1][1]
    for k in range(10):
        dp[j][k] = (dp[j-1][k-1]+dp[j-1][k+1])%1000000000

for m in range(10):
    summ += int(dp[N][m])

print(summ % 1000000000, end='')
