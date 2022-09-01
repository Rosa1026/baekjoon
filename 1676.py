import sys
from math import factorial

N = int(sys.stdin.readline())
a = str(factorial(N))
cnt = 0
i = -1

while i > -len(a):
    if int(a[i]) == 0:
        cnt += 1
    else:
        break
    i -= 1

print(cnt)