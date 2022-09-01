import sys

T = int(sys.stdin.readline())

for _ in range(T):
    N = int(sys.stdin.readline())
    h = 0
    gpa = 0
    for _ in range(N):
        c, g = map(str, sys.stdin.readline().split())
        h += int(c)
        gpa += float(c)*float(g)
    gpa = round(gpa/h, 1)
    print(h, gpa)