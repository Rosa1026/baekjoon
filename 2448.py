import sys

N = int(sys.stdin.readline())
graph = [[' ']*((2*N)-1) for _ in range(N)]

def star(x,y,N):
    if N == 3:
        graph[x][y] = '*'
        graph[x+1][y-1] = graph[x+1][y+1] = '*'
        for i in range(-2,3):
            graph[x+2][y+i] = '*'

    else:
        N = N // 2
        star(x, y, N)
        star(x+N, y-N, N)
        star(x+N, y+N, N)

star(0, N-1, N)
for i in graph:
    print("".join(i))