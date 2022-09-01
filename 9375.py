import sys
from collections import Counter

T = int(sys.stdin.readline())

for _ in range(T):
    N = int(sys.stdin.readline())
    lst = []
    for _ in range(N):
        a, b = map(str, sys.stdin.readline().split())
        lst.append(b)

    cnt = 1
    result = Counter(lst)
    for i in result:
        cnt *= result[i] + 1
    print(cnt - 1)