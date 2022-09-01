import sys

T = int(sys.stdin.readline().rstrip())

a = [list(sys.stdin.readline().split()) for _ in range(T)]

for k in range(T):
    for j in range(len(a[k][1])):
        for i in range(int(a[k][0])):
            print(a[k][1][j], end='')
    print('')