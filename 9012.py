import sys

T = int(sys.stdin.readline())

for _ in range(T):
    cnt = 0
    err = 0
    str = sys.stdin.readline().rstrip()
    lst = list(str)
    for i in lst:
        if cnt == 0:
            if i =='(':
                cnt += 1
            if i == ')':
                print('NO')
                err += 1
                break
        else:
            if i == '(':
                cnt += 1
            elif i == ')':
                cnt -= 1
            if cnt < 0:
                print('NO')
                err += 1
                break

    if cnt > 0:
        print('NO')
    elif cnt == 0 and err == 0:
        print('YES')