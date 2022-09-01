import sys

N = int(sys.stdin.readline())
lst = [[], [], []]
score = []

for _ in range(N):
    a, b, c = map(int, sys.stdin.readline().split())
    lst[0].append(a)
    lst[1].append(b)
    lst[2].append(c)

for i in range(N):
    a_score = 0
    for j in range(3):
        if lst[j].count(lst[j][i]) == 1:
            a_score += lst[j][i]
    score.append(a_score)

for i in score:
    print(i)