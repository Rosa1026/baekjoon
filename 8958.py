import sys

N = int(sys.stdin.readline())
list = [list(sys.stdin.readline().rstrip()) for _ in range(N)]

for i in range(N):
    cnt = 0
    score = [0 for k in range(len(list[i]))]
    for j in range(len(list[i])):
        if list[i][j] == 'O':
            cnt += 1
            score[j] = cnt
        else:
            cnt = 0
    print(sum(score))