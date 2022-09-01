import sys

N = int(sys.stdin.readline())
k = int(sys.stdin.readline())
start, end = 1, k

while start <= end:
    mid = (start+end)//2
    temp = 0

    for i in range(1, N+1):
        temp += min(mid//i, N)

    if temp >= k:
        ans = mid
        end = mid -1

    else:
        start = mid + 1

print(ans)