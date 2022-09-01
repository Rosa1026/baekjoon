import sys

N = int(sys.stdin.readline())
res = 0

for i in range(N+1, N**2, N+1):
    res += i

print(res)