import sys

N = int(sys.stdin.readline())

sum = 0

for i in range(0, N+1):
    for j in range(i, N+1):
        sum += i + j

print(sum)