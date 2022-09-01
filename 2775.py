import sys

T = int(sys.stdin.readline())

for i in range(T):
    k = int(sys.stdin.readline())
    n = int(sys.stdin.readline())

    floor = [i for i in range(1, n+1)]
    for j in range(k):
        for l in range(1,n):
            floor[l]+=floor[l-1]
    print(floor[-1])