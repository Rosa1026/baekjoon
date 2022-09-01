import sys

N = int(sys.stdin.readline())

for i in range(N):
    for j in range(i):
        print(' ', end='')
    for j in range(N*2-(i*2+1),0,-1):
        print('*', end='')
    print()