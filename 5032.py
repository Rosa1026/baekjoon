import sys

e, f, c = map(int, sys.stdin.readline().split())
res = 0
cur = e + f

while cur >= c:
    res += cur//c
    cur = cur//c + cur%c

print(res)