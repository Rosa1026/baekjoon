import sys

N = int(sys.stdin.readline())
lst = []

for _ in range(N):
    lst.append(sys.stdin.readline().rstrip())

a = set(lst)
lst = list(a)
lst.sort()
lst.sort(key = len)

for i in lst:
    print(i)