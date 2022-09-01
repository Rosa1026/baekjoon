import sys
import math

N, K = map(int, sys.stdin.readline().split())
num = list(map(int, sys.stdin.readline().split()))
Q = int(sys.stdin.readline())

def something(jump, cnt):
    i = 0
    while i < N:
        a[i] = a[i] + cnt
        i = i + jump

for _ in range(Q):
    a = [0 for _ in range(N)]
    res = [0 for _ in range(N)]
    cnt = K
    L, R = map(int, sys.stdin.readline().split())

    b = num.count()
    for i in range(K):
        something(num[i], cnt)

    print(a)
    res[0] = a[0]
    for i in range(1, N):
        res[i] = res[i-1]+a[i]

    if L != 0:
        print(res[R]-res[L-1])

    else:
        print(res[R])