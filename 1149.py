import sys

N = int(sys.stdin.readline())
color = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

for i in range(1, len(color)):
    color[i][0] = min(color[i-1][1], color[i-1][2]) + color[i][0]
    color[i][1] = min(color[i-1][0], color[i-1][2]) + color[i][1]
    color[i][2] = min(color[i-1][0], color[i-1][1]) + color[i][2]

print(min(color[N-1][0], color[N-1][1], color[N-1][2]))