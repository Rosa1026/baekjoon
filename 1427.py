import sys

N = sys.stdin.readline().rstrip()
list = []

for i in range(len(N)):
    list.append(int(N[i]))

list.sort(reverse=True)
for i in range(len(list)):
    print(list[i], end='')