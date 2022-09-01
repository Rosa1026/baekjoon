import sys

T = int(sys.stdin.readline())

for _ in range(T):
    N = int(sys.stdin.readline())
    cnt = 0
    i = 5
    while i <= N:
        cnt += N//i
        i *= 5

    print(cnt)