import sys
from collections import deque

N = int(sys.stdin.readline())
lst = deque([])

if N == 1 or N == 2:
    print(N)

else:
    for i in range(1, N+1):
        lst.append(i)

    n = 1

    while len(lst) > 1:
        if n % 2 == 1:
            lst.popleft()
        else:
            a = lst.popleft()
            lst.append(a)
        n += 1

    print(lst[0])