import sys

N = int(sys.stdin.readline())
lst = []

for _ in range(N):
    age, name = map(str, sys.stdin.readline().split(' '))
    age = int(age)
    name = name.replace("\n", "")
    lst.append((age, name))

lst.sort(key=lambda x: x[0])

for i in lst:
    print(i[0], i[1])