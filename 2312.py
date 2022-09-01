import sys

T = int(sys.stdin.readline())

for _ in range(T):
    N = int(sys.stdin.readline())

    for i in range(2,N+1):
        cnt = 0
        if N % i == 0:
            while N % i == 0:
                N = N//i
                cnt += 1
            print('%d %d' %(i, cnt))

        elif N == 1:
            break