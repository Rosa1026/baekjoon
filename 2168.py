import sys

x, y = map(int, sys.stdin.readline().split())

def gcd(a, b):
    if a < b:
        (a, b) = (b, a)
    while b != 0:
        (a, b) = (b, a % b)
    return a

print(x+y-gcd(x,y))