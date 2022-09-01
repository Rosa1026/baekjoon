import sys

W = []
K = []
for _ in range(10):
    W.append(int(sys.stdin.readline()))

for _ in range(10):
    K.append(int(sys.stdin.readline()))

W.sort()
K.sort()

W_score = 0
K_score = 0

for i in range(-1, -4, -1):
    W_score += W[i]
    K_score += K[i]

print(W_score, K_score)
