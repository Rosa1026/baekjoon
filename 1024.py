import sys

N, L = map(int, sys.stdin.readline().split())
x = -1
for i in range(L, 101):
    k = (i*i - i)/2
    if (N - k) % i == 0 and (N - k)//i >= 0:
        x = (N - k) // i
        length = i
        break

if x == -1:
    print(-1)
else:
    for i in range(length):
        print(int(x + i), end=' ')