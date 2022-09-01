import sys

N = int(sys.stdin.readline())
lst = list(map(int, sys.stdin.readline().split()))

lst.sort()
result = 0
for i in range(N):
    result += lst[i]*(N-i)

print(result)