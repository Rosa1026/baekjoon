import sys

N = int(sys.stdin.readline())

A = [list(map(int, input())) for _ in range(N)]

def check(N,x,y):
    ok = A[x][y]
    for i in range(x, x+N):
        for j in range(y, y+N):
            if ok != A[i][j]:
                ok = -1
                break

    if ok == -1:
        print("(", end='')
        N = N//2
        check(N, x, y)
        check(N, x, y+N)
        check(N, x+N, y)
        check(N, x+N, y+N)
        print(")", end='')

    elif ok == 1:
        print(1, end='')

    else:
        print(0, end='')

check(N, 0, 0)