import sys

A = list(map(int, sys.stdin.readline().split()))
A.sort()

if A[1] - A[0] == A[2] - A[1]:
    print(A[2]+A[2]-A[1])

elif A[1] - A[0] == (A[2] - A[1])*2:
    print(A[0]+A[2]-A[1])

elif (A[1] - A[0])*2 == A[2] - A[1]:
    print(A[1] + A[1] - A[0])