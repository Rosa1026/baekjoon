import sys

S = sys.stdin.readline().rstrip()
a = list(range(97,123))

for x in a:
    print(S.find(chr(x)), end=' ')