import sys

N = int(sys.stdin.readline())
A = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
result = [0, 0 ,0]

def check(x, y, z):
    temp = A[x][y]
    for i in range(z):
        for j in range(z):
            if temp != A[x + i][y + j]:
                return False

    return True

def divide(x, y, z):
    if check(x, y, z):
        result[A[x][y]+1] += 1
    else:
        for i in range(3):
            for j in range(3):
                divide(x + i*z//3, y + j*z//3, z//3)
    return

divide(0, 0, N)
for i in range(3):
    print(result[i])