import sys

T = int(sys.stdin.readline())
dp = [0 for _ in range(1, 102)]

dp[1] = 1
dp[2] = 1
dp[3] = 1
dp[4] = 2
dp[5] = 2

for _ in range(T):
    N = int(sys.stdin.readline())

    for k in range(6, N+1):
        dp[k] = dp[k-1] + dp[k-5]

    print(dp[N])