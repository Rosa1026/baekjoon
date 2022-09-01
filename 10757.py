import sys

A, B = sys.stdin.readline().split()

if len(A) > len(B):
    x = len(B)
else:
    x = len(A)

z = [0 for i in range(x+1)]

for i in range(x):
    y = int(A[x-i-1]) + int(B[x-i-1])
    if y >= 10:
        z[x-i] += y % 10
        z[x-i-1] += 1
    else:
        z[x-i] += y

for i in range(len(z)):
    print(z[i], end='')
#
# import sys
#
# A, B = map(int, sys.stdin.readline().split())
#
# print(A+B)