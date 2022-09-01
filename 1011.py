import sys

T = int(sys.stdin.readline())

for _ in range(T):
    x, y = map(int, sys.stdin.readline().split())
    length = y - x
    cnt = 0
    move = 0
    plus = 1

    while move < length:
        cnt += 1
        move += plus
        if cnt % 2 == 0:
            plus += 1

    print(cnt)