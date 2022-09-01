import sys

A,B = [int(x) for x in sys.stdin.readline().split()]

if A>B:
    print('>')
elif A<B:
    print('<')
else:
    print('==')