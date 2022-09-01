import sys

X, Y = map(str, sys.stdin.readline().split())

res = str(int(X[::-1])+int(Y[::-1]))
print(int(res[::-1]))