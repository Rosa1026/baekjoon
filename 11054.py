import sys

N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))
dp_inc = [0 for _ in range(N)]
dp_dec = [0 for _ in range(N)]
res = [0 for _ in range(N)]

for i in range(N):
    for j in range(i):
        if A[i] > A[j] and dp_inc[i] < dp_inc[j]:
            dp_inc[i] = dp_inc[j]
    dp_inc[i] += 1

for i in range(N-1, -1, -1):
    for j in range(N-1, i, -1):
        if A[i] > A[j] and dp_dec[i] < dp_dec[j]:
            dp_dec[i] = dp_dec[j]
    dp_dec[i] += 1

for i in range(N):
    res[i] = dp_inc[i] + dp_dec[i] -1
print(max(res))