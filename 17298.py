import sys

N = int(sys.stdin.readline())
num_lst = list(map(int, sys.stdin.readline().split()))
ans_lst = [-1]*N
stk = []

for i in range(N):
    while stk and num_lst[stk[-1]] < num_lst[i]:
        ans_lst[stk.pop()] = num_lst[i]
    stk.append(i)

print(*ans_lst)