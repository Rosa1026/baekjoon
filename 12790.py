import sys
from collections import Counter

T = int(sys.stdin.readline())

for _ in range(T):
    lst = list(map(int, sys.stdin.readline().split()))

    HP = lst[0] + lst[4]
    MP = lst[1] + lst[5]
    ATK = lst[2] + lst[6]
    DEF = lst[3] + lst[7]

    if HP < 1:
        HP = 1

    if MP < 1:
        MP = 1

    if ATK < 0:
        ATK = 0

    print((1*HP)+(5*MP)+(2*ATK)+(2*DEF))