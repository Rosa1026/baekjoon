import sys

N = int(sys.stdin.readline())

len = 1
x = 1

if N == 1:
    print('1/1')

while N > len:
    len += x
    x += 1

print('x-1')