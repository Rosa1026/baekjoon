import sys

N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))
B = list(map(int, sys.stdin.readline().split()))

A.sort(reverse=True)
s = 0

B = sorted(B)

for i in range(N):
    s += A[i]*B[i]

print(s)