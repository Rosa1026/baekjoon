import sys
from collections import Counter

N = int(sys.stdin.readline())
list = []

for _ in range(N):
    list.append(int(sys.stdin.readline()))

list.sort()
list_s = Counter(list).most_common()
plus_avg = round(sum(list) / N)
MID = list[int(N//2)]
range = list[-1] - list[0]

print(plus_avg)
print(MID)
if len(list_s) > 1:
    if list_s[0][1] > 1:
        if list_s[1][1] > 1:
            if list_s[0][1] == list_s[1][1]:
                print(list_s[1][0])
            else:
                print(list_s[0][0])
        else:
            if list_s[0][1] == list_s[1][1]:
                print(list_s[1][0])
            else:
                print(list_s[0][0])
    else:
        if list_s[0][1] == list_s[1][1]:
            print(list_s[1][0])
        else:
            print(list_s[0][0])
else:
    print(list_s[0][0])

print(range)