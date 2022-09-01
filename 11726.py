import sys

N = int(sys.stdin.readline())

dp = [0 for i in range(1001)]

dp[1] = 1
dp[2] = 2

j = 3
while j <= N:
    dp[j] = (dp[j-1]+dp[j-2]) % 10007
    j += 1

print(dp[N])