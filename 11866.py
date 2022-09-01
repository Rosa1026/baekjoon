import sys
from collections import deque

N, K = map(int, sys.stdin.readline().split())
lst = []
lst_s = []

for i in range(1, N+1):
    lst.append(i)

n = K-1

while len(lst) > 0:
    if n >= len(lst):
        while n >= len(lst):
            n = n - len(lst)
    a = lst[n]
    lst.remove(a)
    lst_s.append(a)

    n += K-1

print('<', end='')
for i in range(len(lst_s)-1):
    print(lst_s[i], end=', ')

print('{}>' .format(lst_s[-1]))