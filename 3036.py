import sys

N = int(sys.stdin.readline())
lst = list(map(int, sys.stdin.readline().split()))
M_lst = []

def gcd(a, b):
    while b > 0:
        a, b = b, a % b
    return a

for i in range(1,N):
    a = gcd(lst[0], lst[i])
    M_lst.append('{0}/{1}'.format(lst[0]//a, lst[i]//a))

for i in M_lst:
    print(i)