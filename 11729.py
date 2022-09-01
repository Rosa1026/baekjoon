import sys

N = int(sys.stdin.readline())

def hanoi(N, a, b, c):
    if N == 1:
        print(a, c)
    else:
        hanoi(N-1, a, c, b)
        print(a, c)
        hanoi(N-1, b, a, c)

sum = 0
for i in range(N):
    sum = sum * 2 + 1

print(sum)
hanoi(N, 1, 2, 3)