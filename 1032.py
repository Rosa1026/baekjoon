import sys

N = int(sys.stdin.readline())
lst = list(sys.stdin.readline().rstrip())

for _ in range(N-1):
    che = list(sys.stdin.readline().rstrip())
    for j in range(len(lst)):
        if lst[j] != che[j]:
            lst[j] = '?'

print("".join(lst))