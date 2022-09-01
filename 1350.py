import sys

N = int(sys.stdin.readline())
F = list(map(int, sys.stdin.readline().split()))
C = int(sys.stdin.readline())
s = 0

for i in F:
    if i != 0:
        if i%C == 0:
            a = i//C
        else:
            a = i//C + 1

        s += a*C

print(s)