import sys

def prime(n):
    if n == 1:
        return False

    for j in range(2,int(n**0.5)+1):
        if n % j == 0:
            return False
    return True

all = list(range(2,246912))
sosu = []

for i in all:
    if prime(i):
        sosu.append(i)

while True:
    N = int(sys.stdin.readline())
    cnt = 0
    if N == 0:
        break

    for i in sosu:
        if N < i < 2*N+1:
            cnt += 1
    print(cnt)