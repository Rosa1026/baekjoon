import sys

N = int(sys.stdin.readline())
lst = []

for _ in range(N):
    stack = list(map(str, sys.stdin.readline().split()))

    if stack[0] == 'push':
        lst.append(int(stack[1]))

    if stack[0] == 'top':
        if len(lst) == 0:
            print('-1')
        else:
            print(lst[-1])

    if stack[0] == 'size':
        print(len(lst))

    if stack[0] == 'empty':
        if len(lst) == 0:
            print('1')
        else:
            print('0')

    if stack[0] == 'pop':
        if len(lst) == 0:
            print('-1')
        else:
            print(lst[-1])
            del lst[-1]