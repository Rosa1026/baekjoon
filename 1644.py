import sys

n = int(sys.stdin.readline())

lst = []
a = [False, False] + [True]*(n-1)

for i in range(2, n+1):
    if a[i]:
        lst.append(i)
        for j in range(2*i, n+1, i):
            a[j] = False

ans = 0
start = 0
end = 1

while end <= len(lst):
    temp = sum(lst[start:end])
    if temp == n:
        ans += 1
        end += 1
    elif temp < n:
        end += 1
    else:
        start += 1

print(ans)