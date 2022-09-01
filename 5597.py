import sys

lst = [0 for _ in range(31)]

for _ in range(28):
    i = int(sys.stdin.readline())
    lst[i] += 1

for i in range(1,len(lst)):
    if lst[i] != 1:
        print(i)