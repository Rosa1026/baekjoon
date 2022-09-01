import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())
idx = list(map(int, sys.stdin.readline().split()))
lst = deque(list(range(1, N+1)))

cnt = 0

for i in idx:
    while True:
        if lst[0] == i:
            lst.popleft()
            break
        else:
            if lst.index(i) < len(lst)/2:
                while lst[0] != i:
                    lst.append(lst.popleft())
                    cnt += 1
            else:
                while lst[0] != i:
                    lst.appendleft(lst.pop())
                    cnt += 1

print(cnt)