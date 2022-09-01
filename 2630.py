import sys

N = int(sys.stdin.readline())
lst = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

cnt_w = 0
cnt_b = 0

def paper(x,y,N):
    global cnt_w, cnt_b
    a = lst[x][y]
    for i in range(x, x+N):
        for j in range(y, y+N):
            if a != lst[i][j]:
                paper(x,y,N//2)
                paper(x,y+N//2,N//2)
                paper(x+N//2,y,N//2)
                paper(x+N//2,y+N//2,N//2)
                return

    if a == 0:
        cnt_w += 1
        return
    else:
        cnt_b += 1
        return

paper(0,0,N)
print(cnt_w)
print(cnt_b)