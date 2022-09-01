import sys

alpha = ['c=','c-','dz=','d-','lj','nj','s=','z=']
c = []
N1 = sys.stdin.readline().rstrip()
cnt = len(N1)

for i in range(len(N1)-1):
    for j in alpha:
        if N1[i]+N1[i+1] in j:
            c.append(i)
            break


for i in range(len(N1)):
    if i in c:
        cnt -= 1

print(cnt, end='')