import sys
from collections import deque

T = int(sys.stdin.readline())

for _ in range(T):
    p = sys.stdin.readline().rstrip()
    n = int(sys.stdin.readline())
    lst = deque(sys.stdin.readline().rstrip()[1:-1].split(","))

    if n == 0:
        lst = deque()
    r = 0
    err = 0
    for i in p:
        if i == 'R':
            r += 1
        elif i == 'D':
            if len(lst) == 0:
                print('error')
                err += 1
                break
            else:
                if r % 2 == 0:
                    lst.popleft()
                else:
                    lst.pop()
    if err == 0:
        if r % 2 == 0:
            print("["+",".join(lst)+"]")
        else:
            lst.reverse()
            print("[" + ",".join(lst) + "]")