import sys

N = int(sys.stdin.readline())
list = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

for j in range(N):
    avg = sum(list[j][1:])/list[j][0]
    cnt = 0
    for i in range(1, len(list[j])):
        if list[j][i] > avg:
            cnt += 1
    rate = cnt/list[j][0]*100
    print(f'{rate:.3f}%')