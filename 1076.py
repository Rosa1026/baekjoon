import sys

color = ['black','brown','red','orange','yellow','green','blue','violet','grey','white']
fir = color.index(sys.stdin.readline().rstrip())
sec = color.index(sys.stdin.readline().rstrip())
thi = color.index(sys.stdin.readline().rstrip())

print(int(str(fir)+str(sec))*(10**int(thi)))