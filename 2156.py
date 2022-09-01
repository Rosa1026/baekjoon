import sys

N = int(sys.stdin.readline())
s = [0]

for i in range(N):
    s.append(int(sys.stdin.readline()))

dp = [0]
dp.append(s[1])
if N > 1:
    dp.append(s[1] + s[2])
for i in range(3, N + 1):
    dp.append(max(dp[i - 1], dp[i - 3] + s[i - 1] + s[i], dp[i - 2] + s[i]))
print(dp[N], end='')