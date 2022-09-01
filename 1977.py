import sys

M = int(sys.stdin.readline())
N = int(sys.stdin.readline())
lst = []
i = 1
res = 0

while i ** 2 <= N:
    if M <= i ** 2 <= N:
        lst.append(i)
        i += 1

    else:
        i += 1

for i in lst:
    res += i ** 2

if len(lst) != 0:
    print(res)
    print(lst[0]**2)

else:
    print(-1)