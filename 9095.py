import sys

T = int(sys.stdin.readline()) #테스트 케이스 개수

inp = [0 for k in range(T)]
dp = [0 for k in range(11)]

i = 0
m = 1
j = 4

while i < T:
    N = int(sys.stdin.readline()) #정수 받음
    inp[i] = N
    i += 1

dp[1] = 1
dp[2] = 2
dp[3] = 4

for i in inp:
    if i < 4:
        print(dp[i])

    else:
        while j <= i:
            dp[j] = dp[j-1]+dp[j-2]+dp[j-3]
            j += 1
        print(dp[i])