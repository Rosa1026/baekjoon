import sys

N = int(sys.stdin.readline())
time = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

time = sorted(time, key=lambda a:a[0])
time = sorted(time, key=lambda a:a[1])
last = 0
cnt = 0

for i,j in time:
    if i >= last:
        cnt += 1
        last = j

print(cnt)