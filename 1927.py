import sys
import heapq

N = int(sys.stdin.readline())
lst = []

for _ in range(N):
    x = int(sys.stdin.readline())

    if x == 0:
        if len(lst) == 0:
            print(0)
        else:
            print(heapq.heappop(lst))

    else:
        heapq.heappush(lst, x)