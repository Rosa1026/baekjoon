import sys
from collections import deque

N = int(sys.stdin.readline())
lst = deque([])

for _ in range(N):
    str = sys.stdin.readline().split()

    if str[0] == 'push':
        lst.append(str[1])

    elif str[0] == 'size':
        print(len(lst))

    elif str[0] == 'empty':
        if len(lst) == 0:
            print(1)
        else:
            print(0)

    elif str[0] == 'pop':
        if len(lst) == 0:
            print(-1)
        else:
            print(lst.popleft())

    elif str[0] == 'front':
        if len(lst) == 0:
            print(-1)
        else:
            print(lst[0])

    elif str[0] == 'back':
        if len(lst) == 0:
            print(-1)
        else:
            print(lst[-1])