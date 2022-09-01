import sys

T = int(sys.stdin.readline())

def gcd(a, b):
    while b > 0:
        a, b = b, a % b
    return a

def lcm(a, b):
    return a * b // gcd(a, b)

for _ in range(T):
    N, M = map(int, sys.stdin.readline().split())

    print(lcm(N, M))