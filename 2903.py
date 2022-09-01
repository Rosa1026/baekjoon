import sys

N = int(sys.stdin.readline())
dp = [0 for _ in range(N+1)]

dp[0] = 2
dp[1] = 3
for i in range(2, N+1):
    dp[i] = dp[i-1]*2 - 1

print(dp[N]**2)