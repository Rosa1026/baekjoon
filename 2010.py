import sys

N = int(sys.stdin.readline())
lst = []
res = 1
for _ in range(N):
    lst.append(int(sys.stdin.readline()))

for i in lst:
    if i > N:
        res += i - N
        N = 0

    else:
        N = N - i

print(res)