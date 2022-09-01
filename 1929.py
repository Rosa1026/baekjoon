import sys

M, N = map(int, sys.stdin.readline().split())

def prime(n):
    if n == 1:
        return False
    else:
        for j in range(2,int(n**0.5)+1):
            if n % j == 0:
                return False
        return True

for i in range(M, N+1):
    if prime(i):
        print(i)