import sys

N, W, H = map(int, sys.stdin.readline().split())

for _ in range(N):
    a = int(sys.stdin.readline())

    if a > (W**2+H**2)**(1/2):
        print('NE')

    else:
        print('DA')