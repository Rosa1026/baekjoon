import sys

N = int(sys.stdin.readline())
lst = [list(sys.stdin.readline().rstrip()) for _ in range(N)]
cnt = N

for i in range(N):
    a = []
    for j in lst[i]:
        if j in a and j != a[-1]:
            cnt -= 1
            break

        a.append(j)

print(cnt)