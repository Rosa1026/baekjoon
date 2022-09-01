import sys
from collections import deque

N = int(sys.stdin.readline())
lst = deque([])

for _ in range(N):
    str = sys.stdin.readline().split()

    if str[0] == 'push_back':
        lst.append(str[1])

    if str[0] == 'push_front':
        lst.appendleft(str[1])

    elif str[0] == 'size':
        print(len(lst))

    elif str[0] == 'empty':
        if len(lst) == 0:
            print(1)
        else:
            print(0)

    elif str[0] == 'pop_front':
        if len(lst) == 0:
            print(-1)
        else:
            print(lst.popleft())

    elif str[0] == 'pop_back':
        if len(lst) == 0:
            print(-1)
        else:
            print(lst.pop())

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