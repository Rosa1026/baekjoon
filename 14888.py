import sys

N = int(sys.stdin.readline())
lst = list(map(int, sys.stdin.readline().split()))
op = list(map(int, sys.stdin.readline().split()))

maxi = -1e9
mini = 1e9

def dfs(dep, total, p, m, g, d):
    global maxi, mini
    if dep == N:
        maxi = max(total, maxi)
        mini = min(total, mini)
        return

    if p:
        dfs(dep + 1, total + lst[dep], p - 1, m, g, d)
    if m:
        dfs(dep + 1, total - lst[dep], p , m - 1, g, d)
    if g:
        dfs(dep + 1, total * lst[dep], p , m , g - 1, d)
    if d:
        dfs(dep + 1, int(total / lst[dep]), p , m , g, d - 1)

dfs(1, lst[0], op[0], op[1], op[2], op[3])
print(maxi)
print(mini)