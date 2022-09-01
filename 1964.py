import sys

N = int(sys.stdin.readline())

num = 5

for i in range(2, N+1):
    num += 3*i+1

print(num % 45678)