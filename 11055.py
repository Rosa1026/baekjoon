import sys

N = int(sys.stdin.readline())
lst = list(map(int, sys.stdin.readline().split()))
dp = [0 for _ in range(N)]
dp[0] = lst[0]

for i in range(1, N):
    s = []
    for j in range(i - 1, -1, -1):
        if lst[i] > lst[j]:
            s.append(dp[j])

    if not s:
        dp[i] = lst[i]

    else:
        dp[i] = lst[i] + max(s)

print(max(dp))