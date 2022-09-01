import sys

n, m = map(int, sys.stdin.readline().split(':'))

def gcd(a, b):
    while b > 0:
        temp = a
        a = b
        b = temp % a
    return a

print('%d:%d' %(n//gcd(n,m),m//gcd(n,m)))