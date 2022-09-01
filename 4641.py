import sys

while True:
    a = list(map(int, sys.stdin.readline().split()))
    cnt = 0

    if len(a) == 1 and -1 in a:
        break

    a = sorted(a, reverse=False)
    for i in range(1, len(a)):
        for j in range(i, len(a)):
            if a[j]/2 == a[i]:
                cnt += 1
    print(cnt)