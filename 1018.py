import sys

N, M = map(int, sys.stdin.readline().split())
lst = [list(sys.stdin.readline().rstrip()) for _ in range(N)]

cnt = []

for i in range(N - 7):
    for j in range(M - 7):
        idx1 = 0
        idx2 = 0
        for k in range(i, i+8):
            for l in range(j, j+8):
                if (k+l)%2 == 0:
                    if lst[k][l] != 'W':
                        idx1 += 1
                    if lst[k][l] != 'B':
                        idx2 += 1

                else:
                    if lst[k][l] != 'B':
                        idx1 += 1
                    if lst[k][l] != 'W':
                        idx2 += 1

        cnt.append(idx1)
        cnt.append(idx2)

print(min(cnt))