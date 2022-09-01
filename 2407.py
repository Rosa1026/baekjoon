import sys
import math

N, M = map(int, sys.stdin.readline().split())

a = math.factorial(N) // (math.factorial(N-M)*math.factorial(M))

print(a)