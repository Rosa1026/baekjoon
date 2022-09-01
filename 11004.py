import sys

N, K = map(int, sys.stdin.readline().split())
A = list(map(int, sys.stdin.readline().split()))

A = sorted(A, reverse=False)

print(A[K-1])