import sys

N = int(sys.stdin.readline())
res = 1
cnt = 2

for _ in range(9, N, 3):
    res = res + cnt
    cnt += 1

print(res)