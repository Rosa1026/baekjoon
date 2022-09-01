import sys

while True:
    N = sys.stdin.readline().rstrip()
    op = []
    err = 0

    if N == '.':
        break

    for i in N:
        if i == '(' or i == '[':
            op.append(i)
            continue

        elif i == ')':
            if len(op) == 0 or op[-1] == '[':
                err += 1
                break

            elif op[-1] == '(':
                op.pop()

        elif i == ']':
            if len(op) == 0 or op[-1] == '(':
                err += 1
                break

            elif op[-1] == '[':
                op.pop()

    if err == 0 and len(op) == 0:
        print('yes')

    else:
        print('no')