import sys

N, M = map(int, sys.stdin.readline().split())

s = []

def dfs(j):
    if len(s) == M:
        print(' '.join(map(str, s)))
        return

    for i in range(j, N+1):
        if i not in s:
            s.append(i)
            dfs(i)
            s.pop()

dfs(1)