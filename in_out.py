T = int(input())
a = []
b = []
c = []
i = 0

while i < T:
    A = input()
    a.append(A)
    B = A.split(' ')[0]
    C = A.split(' ')[1]
    b.append(int(B))
    c.append(int(C))
    i += 1

i = 0

while i < T:
    print(b[i]+c[i])
    i += 1