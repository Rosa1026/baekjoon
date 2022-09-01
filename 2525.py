import sys

A, B = map(int, sys.stdin.readline().split())
C = int(sys.stdin.readline())
D = B+C

if D >= 60:
    A += D // 60
    D -= 60 * (D // 60)

if A >= 24:
    A = A - 24

print(A, D)