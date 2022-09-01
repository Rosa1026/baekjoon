import sys

N = int(sys.stdin.readline())

lst = list(map(int, sys.stdin.readline().split()))
M = []
Y = []

for i in lst:
    if i//30 == 0 and i > 30:
        a = (i//30)*10
    elif i//30 != 0 or i < 30:
        a = (i//30 + 1)*10

    if i//60 == 0 and i > 60:
        b = (i//60)*15

    elif i//60 != 0 or i < 60:
        b = (i//60 + 1)*15

    Y.append(a)
    M.append(b)

if sum(Y) < sum(M):
    print('Y', end=' ')
    print(sum(Y))

elif sum(Y) > sum(M):
    print('M', end=' ')
    print(sum(M))

else:
    print('Y M', end=' ')
    print(sum(Y))