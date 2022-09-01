import sys

N = int(sys.stdin.readline())
stair_lst = [0 for _ in range(301)]
dp = [0 for _ in range(301)]

for i in range(N):
    stair_lst[i] = int(sys.stdin.readline())

dp[0] = stair_lst[0]
dp[1] = stair_lst[0]+stair_lst[1]
dp[2] = max(stair_lst[1]+stair_lst[2], stair_lst[0]+stair_lst[2])

for i in range(3, N):
    dp[i] = max(dp[i-3]+stair_lst[i-1]+stair_lst[i], dp[i-2]+stair_lst[i])

print(dp[N-1])