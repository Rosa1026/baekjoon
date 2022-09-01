import sys

A, B, C = map(int, sys.stdin.readline().split())

def multiple(A,B,C):
    if B == 1:
        return A%C

    else:
        mid = multiple(A,B//2,C)
        if B % 2 == 0:
            return mid*mid%C
        else:
            return mid*mid*A%C

print(multiple(A,B,C))