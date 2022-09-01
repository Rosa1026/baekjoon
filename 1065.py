import sys

N = sys.stdin.readline().rstrip()
M = int(N)

def hansoo(N, M):
    cnt = 0
    if len(N) == 1 or len(N) == 2:
        cnt = M
    else:
        cnt = 99
        for i in range(100, M+1):
            a = i // 100
            b = (i % 100) // 10
            c = (i % 100) % 10
            if a - b == b - c:
                cnt += 1
    print(cnt)

hansoo(N, M)