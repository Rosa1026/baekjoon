import sys

N = int(sys.stdin.readline())

for i in range(2*N-1):
    if i < N:
        for j in range(i):
            print(' ', end='')
        for j in range(2*(N-i)-1,0,-1):
            print('*', end='')

    else:
        for j in range(2*N-i-2,0,-1):
            print(' ', end='')
        for j in range(2*(i-N)+3):
            print('*', end='')
    print()