import sys

X, Y = map(int, sys.stdin.readline().split())
N = int(sys.stdin.readline())
goal = X * 1000/Y

for i in range(N):
    x, y = map(int, sys.stdin.readline().split())

    goal = min(goal, x*1000/y)

print(round(goal, 2))