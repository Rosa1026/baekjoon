import sys

N = int(sys.stdin.readline())
B_lst = list(map(int, sys.stdin.readline().split()))
A_lst = [0 for _ in range(N)]

A_lst[0] = B_lst[0]

for i in range(1, len(B_lst)):
    A_lst[i] = B_lst[i] * (i+1) - sum(A_lst)

for i in A_lst:
    print(i, end=' ')