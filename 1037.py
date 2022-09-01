import sys

N = int(sys.stdin.readline())
M = list(map(int, sys.stdin.readline().split()))
M.sort()

if N == 0:
    print(N)

elif N == 1:
    print(M[0]**2)
else:
    print(M[0]*M[-1])