import sys

T = int(sys.stdin.readline())

for _ in range(T):
    M, N, x, y = map(int, sys.stdin.readline().split())

    cur_x = 1
    cur_y = 1
    k = 1

    while cur_x != M or cur_y != N:
        if cur_x == M:
            cur_x = 0

        if cur_y == N:
            cur_y = 0

        cur_x += 1
        cur_y += 1
        k += 1

        if cur_x == x and cur_y == y:
            print(k)
            break

    if cur_x != x and cur_y != y:
        print(-1)