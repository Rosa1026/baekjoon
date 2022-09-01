import sys

X = int(sys.stdin.readline())
n = 0
max = 0

while X > max:
    n += 1
    max += n

num = max - X
if n % 2 == 0:
    son = n - num
    mom = num + 1
else:
    son = num + 1
    mom = n - num

print(f'{son}/{mom}')