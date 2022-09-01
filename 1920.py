import sys

N = int(sys.stdin.readline())
N_lst = list(map(int, sys.stdin.readline().split()))
M = int(sys.stdin.readline())
M_lst = list(map(int, sys.stdin.readline().split()))

N_lst.sort()

def search(i, lst, start, end):
    if start > end:
        return 0

    m = (start+end) // 2

    if i == lst[m]:
        return 1

    elif i < lst[m]:
        return search(i, N_lst, start, m-1)

    else:
        return search(i, N_lst, m+1, end)

for i in M_lst:
    start = 0
    end = N - 1
    print(search(i, N_lst, start, end))