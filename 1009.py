import sys

T = int(sys.stdin.readline())

for _ in range(T):
    a, b = map(int, sys.stdin.readline().split())
    a = a % 10

    if a == 0:
        k = 10

    elif a in [1, 5, 6]:
        k = a

    elif a in [4, 9]:
        b = b % 2
        if b == 1:
            k = a
        else:
            k = ((a * a) % 10)
    else:
        b = b % 4
        if b == 0:
            k = (a ** 4) % 10

        else:
            k = (a ** b) % 10

    print(k)