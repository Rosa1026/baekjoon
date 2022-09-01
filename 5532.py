import sys
import math

L = int(sys.stdin.readline())
A = int(sys.stdin.readline())
B = int(sys.stdin.readline())
C = int(sys.stdin.readline())
D = int(sys.stdin.readline())

a = math.ceil(A/C)
b = math.ceil(B/D)
print(L - max(a,b))