import sys

A = []
a = 0
b = 0

for i in range(9):
    N = int(sys.stdin.readline())
    A.append(N)

for i in range(9):
    if A[i] > a:
        a = A[i]
        b = i+1

print(a)
print(b)