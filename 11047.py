import sys

N, K = map(int, sys.stdin.readline().split())
lst = []
cnt = 0

for _ in range(N):
    a = int(sys.stdin.readline())
    if a <= K:
        lst.append(a)

def check(n, k):
    global cnt
    for i in reversed(range(len(lst))):
        cnt += k//lst[i]
        k = k%lst[i]

check(N, K)
print(cnt)