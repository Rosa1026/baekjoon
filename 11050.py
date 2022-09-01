import sys

N, K = map(int, sys.stdin.readline().split())

def fac(a):
    if a == 1:
        return 1
    a = a * fac(a-1)
    return a

if K == 0:
    print(fac(N)//fac(N-K))
elif N-K == 0:
    print(fac(N)//fac(K))
else:
    print(fac(N)//(fac(K)*fac(N-K)))