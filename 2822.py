import sys

lst = []
num = []
lst.append(int(sys.stdin.readline()))
num.append(0)

for i in range(1,8):
    a = int(sys.stdin.readline())
    if len(lst) < 5:
        lst.append(a)
        num.append(i)

    else:
        if a > min(lst):
            num[lst.index(min(lst))] = i
            lst[lst.index(min(lst))] = a

num.sort()
print(sum(lst))
for i in num:
    print(i+1, end=' ')