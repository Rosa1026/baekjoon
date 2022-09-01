import sys

N, M = map(int, sys.stdin.readline().split())

def count(a, b):
    cnt = 0
    while a != 0:
        a = a // b
        cnt += a
    return cnt

five = count(N, 5) - count(M, 5) - count(N-M,5)
two = count(N, 2) - count(M, 2) - count(N-M, 2)

print(min(five, two))