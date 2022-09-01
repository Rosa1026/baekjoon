import sys

N, M = map(int, sys.stdin.readline().split())
card = list(map(int, sys.stdin.readline().split()))

sum  = 0

card.sort(reverse=True)

for i in range(N):
    for j in range(i+1, N):
        for k in range(j+1, N):
            if card[i]+card[j]+card[k] > M:
                continue
            else:
                sum = max(sum, card[i]+card[j]+card[k])

print(sum)