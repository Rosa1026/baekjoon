import sys

T = int(sys.stdin.readline())

for _ in range(T):
    k = int(sys.stdin.readline())

    start = 1
    for _ in range(k-1):
        start = start * 2 + 1

    print(start)