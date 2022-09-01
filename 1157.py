import sys

S = sys.stdin.readline().rstrip().lower()
Unique = list(set(S))
cnt = []

for i in Unique:
    count = S.count(i)
    cnt.append(count)

if cnt.count(max(cnt)) >= 2:
    print("?")
else:
    print(Unique[(cnt.index(max(cnt)))].upper())