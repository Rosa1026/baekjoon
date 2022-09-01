import sys

burger = list(int(sys.stdin.readline()) for _ in range(3))
bevarage = list(int(sys.stdin.readline()) for _ in range(2))
lst = []

for i in burger:
    for j in bevarage:
        lst.append(i + j - 50)

print(min(lst))