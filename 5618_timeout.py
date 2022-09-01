import sys

n = int(sys.stdin.readline())
lst = list(map(int, sys.stdin.readline().split()))
res = []

lst.sort()

for i in range(1, lst[0]+1):
    if lst[0]%i == 0:
        res.append(i)

for i in range(1, len(lst)):
    for j in res:
        if lst[i]%j != 0:
            res.remove(j)

for i in res:
    print(i)