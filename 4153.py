import sys

while True:
    lst = list(map(int, sys.stdin.readline().split()))

    if sum(lst) == 0:
        break

    lst_s = sorted(lst, reverse=True)

    if lst_s[0]**2 == lst_s[1]**2 + lst_s[2]**2:
        print('right')

    else:
        print('wrong')