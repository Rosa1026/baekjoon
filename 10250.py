import sys

T = int(sys.stdin.readline())

test = [list(map(int, sys.stdin.readline().split())) for _ in range(T)]

for i in range(T):
    width = test[i][2] // test[i][0] + 1
    height = test[i][2] % test[i][0]

    if height == 0:
        height = test[i][0]
        width -= 1

    print(f'{height*100+width}')