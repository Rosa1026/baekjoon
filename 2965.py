import sys

A, B, C = map(int, sys.stdin.readline().split())

D = max(B-A,C-B)
print(D-1)