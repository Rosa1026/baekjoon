import sys
from collections import deque

T = int(sys.stdin.readline())

for _ in range(T):
    num_l = list(map(int, sys.stdin.readline().split()))
    wei_l = deque(list(map(int, sys.stdin.readline().split())))
    cnt = 0
    a = deque(list(range(len(wei_l))))
    a[num_l[1]] = 'goal'

    if num_l[0] == 1:
        print(1)

    else:
        while True:
            if wei_l[0] < max(wei_l):
                wei_l.append(wei_l.popleft())
                a.append(a.popleft())

            elif wei_l[0] == max(wei_l):
                wei_l.popleft()
                b = a.popleft()
                cnt += 1
                if b == 'goal':
                    break

        print(cnt)