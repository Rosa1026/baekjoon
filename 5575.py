import sys

for _ in range(3):
    lst = list(map(int, sys.stdin.readline().split()))

    h = lst[3] - lst[0]
    m = lst[4] - lst[1]
    s = lst[5] - lst[2]

    if s < 0:
        s += 60
        m -= 1
        if m < 0:
            m += 60
            h -= 1

    else:
        if m < 0:
            m += 60
            h -= 1

    print(h,m,s)