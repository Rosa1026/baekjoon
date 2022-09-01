import sys

while True:
    N, M = map(int, sys.stdin.readline().split())
    if N == 0 and M == 0:
        break

    if N > M:
        if N % M == 0:
            print('multiple')
        else:
            print('neither')
    elif N < M:
        if M % N == 0:
            print('factor')
        else:
            print('neither')