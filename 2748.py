import sys

N = int(sys.stdin.readline())
dp = []

def fibonacci(n):
    num = 0
    for i in range(n+1):
        if i == 0:
            num = 0
        elif i == 1:
            num = 1
        else:
            num = dp[-1] + dp[-2]
        dp.append(num)

    return dp[-1]

print(fibonacci(N))