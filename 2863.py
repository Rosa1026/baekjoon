import sys

a, b = map(int, sys.stdin.readline().split())
c, d = map(int, sys.stdin.readline().split())
score = []
score.append(a/c + b/d)

for _ in range(3):
    k = c
    c = d
    d = b
    b = a
    a = k

    sum = a/c + b/d
    score.append(sum)

print(score.index(max(score)))