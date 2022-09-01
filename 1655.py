import sys
import heapq

N = int(sys.stdin.readline())
left = []
right = []

for i in range(N):
    a = int(sys.stdin.readline())

    if len(left) == len(right):
        heapq.heappush(left, (-a, a))

    else:
        heapq.heappush(right, a)

    if right and left[0][1] > right[0]:
        b = heapq.heappop(right)[0]
        c = heapq.heappop(left)[1]
        heapq.heappush(left, (-b, b))
        heapq.heappush(right, (c, c))

    print(left[0][1])