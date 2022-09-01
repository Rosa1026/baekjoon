import sys
X = []
Y = []

for _ in range(3):
    x, y= map(int, sys.stdin.readline().split())
    X.append(x)
    Y.append(y)

for i in range(3):
    if X.count(X[i]) == 1:
        x = X[i]
    if Y.count(Y[i]) == 1:
        y = Y[i]

print(x, y)