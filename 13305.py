import sys

N = int(sys.stdin.readline())
road = list(map(int, sys.stdin.readline().split()))
gas = list(map(int, sys.stdin.readline().split()))
gas.pop()
result = 0
m = gas[0]

for i in range(N-1):
    if gas[i] < m:
        m = gas[i]
    result += m*road[i]

print(result)