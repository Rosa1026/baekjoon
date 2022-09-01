import sys

n = int(sys.stdin.readline())
lst = list(map(int, sys.stdin.readline().split()))
lst.sort()
answer = []
left, right = 0, n-1
min = 2000000001

while left < right:
    temp = lst[left] + lst[right]
    if min > abs(temp):
        min = abs(temp)
        answer = [lst[left], lst[right]]

    if temp < 0:
        left += 1

    else:
        right -= 1

print(answer[0], answer[1])