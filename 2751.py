import sys

N = int(sys.stdin.readline())

s = []

i = 0
k = 0

while i < N:
    x = int(sys.stdin.readline())
    s.append(x)
    i += 1

s.sort()

while k < N:
    print(s[k])
    k += 1