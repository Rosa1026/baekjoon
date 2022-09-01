import sys

lst = [[0 for _ in range(15)] for _ in range(5)]
res = []

for i in range(5):
    a = list(sys.stdin.readline().rstrip())

    for j in range(len(a)):
        lst[i][j] = a[j]

for i in range(15):
    for j in range(5):
        if lst[j][i] == 0:
            continue
        res.append(lst[j][i])

for i in res:
    print(i, end='')