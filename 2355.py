import sys

A, B = map(int, sys.stdin.readline().split())
res = 0

if abs(B-A) % 2 == 0:
    res += (B+A)*(abs(B-A)//2) + (B+A)//2

else:
    res += (B+A)*(abs(B-A)//2 + 1)

print(res)