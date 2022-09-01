import sys

n = int(sys.stdin.readline())
num = []
stk = []
ans = []

for _ in range(n):
    num.append(int(sys.stdin.readline()))

a = 1
temp = 1

for i in num:
    while a <= i:
        stk.append(a)
        ans.append('+')
        a += 1

    if stk[-1] == i:
        stk.pop()
        ans.append('-')

    else:
        temp = 0

if not temp:
    print('NO')
else:
    for i in ans:
        print(i)