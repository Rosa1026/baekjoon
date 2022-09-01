import sys

N = int(sys.stdin.readline())

def star(n):
    if n == 1:
        return ['*']

    Star = star(n//3)
    L = []

    for S in Star:
        L.append(S*3)
    for S in Star:
        L.append(S+' '*(n//3)+S)
    for S in Star:
        L.append(S*3)
    return L

print('\n'.join(star(N)))