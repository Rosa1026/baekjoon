import sys

n = int(sys.stdin.readline())
lst = list(map(int, sys.stdin.readline().split()))
x = int(sys.stdin.readline())
lst.sort()
cnt = 0
left, right = 0, n-1
while left < right:
    if lst[left] + lst[right] == x:
        cnt += 1
    if lst[left] + lst[right] < x:
        left += 1
        continue
    right -= 1

print(cnt)