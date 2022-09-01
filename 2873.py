import sys

R, C = [int(x) for x in sys.stdin.readline().split()]

A = [list(map(int, sys.stdin.readline().split())) for _ in range(R)]

if R % 2 == 1:
    print(('R'*(C-1)+'D'+'L'*(C-1)+'D')*(R//2)+'R'*(C-1))
elif C % 2 == 1:
    print(('D' * (R - 1) + 'R' + 'U' * (R - 1) + 'R') * (C // 2) + 'D' * (C - 1))
elif R % 2 == 0 and C % 2 == 0:
    pos = [0,0]
    low = 1000
    for i in range(R):
        if i % 2 == 0:
            for j in range(1, C, 2):
                if low > A[i][j]:
                    low = A[i][j]
                    pos = [i,j]
        else:
            for j in range(0, C, 2):
                if low > A[i][j]:
                    low = A[i][j]
                    pos = [i,j]

    result = ('R'*(C-1)+'D'+'L'*(C-1)+'D')*(pos[0]//2)
    