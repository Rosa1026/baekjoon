import sys

n, s = map(int, sys.stdin.readline().split())
lst = list(map(int, sys.stdin.readline().split()))
sum = [0] * (n+1)

for i in range(1, n+1):
    sum[i] = sum[i-1] + lst[i-1]

start, end = 0, 1
length = []

while start != n:
    if sum[end] - sum[start] >= s:
        if end - start < 1000001:
            length.append(end-start)
        start += 1

    else:
        if end != n:
            end += 1
        else:
            start += 1

print(min(length))