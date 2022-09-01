import sys

N = int(sys.stdin.readline())

x = 0
while N >= 0:
    if N % 5 == 0:
        x += (N // 5)
        print(x)
        break
    N -= 3
    x += 1
else:
    print(-1)