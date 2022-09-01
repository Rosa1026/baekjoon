import sys

e, s, m = 1, 1, 1
E, S, M = [int(x) for x in sys.stdin.readline().split()]
count = 1

while(True):
    if (E == e and S == s and M == m):
        break
    else:
        e += 1
        s += 1
        m += 1
        count += 1
        if e > 15:
            e -= 15
        if s > 28:
            s -= 28
        if m > 19:
            m -= 19

print(count, end='')