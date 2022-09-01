import sys

lst = []
Sum = []
score = 0

for _ in range(10):
    a = int(sys.stdin.readline())
    lst.append(a)

for i in lst:
    if score <= 100:
        score += i
        Sum.append(score)

    else:
        break

if abs(Sum[-1] - 100) > abs(Sum[-2] - 100):
    print(Sum[-2])

else:
    print(Sum[-1])