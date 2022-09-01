import sys

N = int(sys.stdin.readline())
lst = list(map(int, sys.stdin.readline().split()))

lst_s = sorted(list(set(lst)))
dic = {lst_s[i] : i for i in range(len(lst_s))}
for i in lst:
    print(dic[i], end=' ')