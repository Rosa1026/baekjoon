import sys

lst = list(sys.stdin.readline().split('-'))
result = []

for i in lst:
    res = 0
    a = i.split('+')
    for j in a:
        res += int(j)
    result.append(res)

a = result[0]
for i in range(1, len(result)):
    a -= result[i]

print(a)