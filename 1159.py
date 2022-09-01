import sys
from collections import Counter

N = int(sys.stdin.readline())
lst = [list(sys.stdin.readline().rstrip()) for _ in range(N)]
fir = []
res = []
cnt = 0

for i in range(N):
    fir.append(lst[i][0])

fir_count = Counter(fir)

for i,j in fir_count.items():
    if j >= 5:
        res.append(i)
        cnt += 1

if cnt == 0:
    print('PREDAJA')
else:
    res.sort()
    for i in res:
        print(i, end='')