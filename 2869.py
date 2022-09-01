import sys

A, B, V = [int(x) for x in sys.stdin.readline().split()]

cnt = (V - B) / (A-B)

print(int(cnt) if cnt == int(cnt) else int(cnt) + 1)