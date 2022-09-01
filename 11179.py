import sys

N = int(sys.stdin.readline())
ans = []
a = 0
while N != 0:
    if N % 2 == 0:
        ans.append(0)

    else:
        ans.append(1)

    N = N // 2

for i in range(len(ans)):
    a += (2**i)*ans[len(ans)-1-i]

print(a)