import sys

N = int(sys.stdin.readline())
T = []
P = []
dp = []

for _ in range(N):
    a, b = map(int, sys.stdin.readline().split())

    T.append(a)
    P.append(b)
    dp.append(b)
dp.append(0)

for i in range(N-1,-1,-1):
    if T[i] + i > N:
        dp[i] = dp[i+1]

    else:
        dp[i] = max(dp[i+1], P[i] + dp[i + T[i]])

print(dp[0])