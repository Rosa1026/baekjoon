import sys

n = int(sys.stdin.readline())
num = list(map(int, sys.stdin.readline().split()))
sum = []
sum.append(num[0])

for i in range(n-1):
    sum.append(max(sum[i]+num[i+1],num[i+1]))

print(max(sum))