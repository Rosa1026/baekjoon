import sys

N = int(sys.stdin.readline())

a = 1000 - N

def check(a):
    cnt = 0
    while a > 0:
        if a >= 500:
            cnt += a // 500
            a = a % 500
        elif a >= 100:
            cnt += a // 100
            a = a % 100
        elif a >= 50:
            cnt += a // 50
            a = a % 50
        elif a >= 10:
            cnt += a // 10
            a = a % 10
        elif a >= 5:
            cnt += a // 5
            a = a % 5
        else:
            cnt += a // 1
            a = a % 1

    print(cnt)

check(a)