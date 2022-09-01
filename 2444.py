import sys

N = int(sys.stdin.readline())

for i in range(1,2*N):
    if i <= N:
        for j in range(N-i,0,-1):
            print(' ', end='')
        for j in range(2*i-1):
            print('*', end='')

    else:
        for j in range(i-N,0,-1):
            print(' ', end='')
        for j in range(2*(2*N-i)-1):
            print('*', end='')
    print()