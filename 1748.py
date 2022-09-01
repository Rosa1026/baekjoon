import sys

N = sys.stdin.readline().rstrip()
res = 0

for i in range(1,len(N)+1):
    if i != len(N):
        res += (9*(10**(i-1)))*i

    else:
        res += (int(N)-(10**(len(N)-1)) + 1)*len(N)

print(res)