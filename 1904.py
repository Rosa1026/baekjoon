import sys

N = int(sys.stdin.readline())

tile_s = [0]*1000001

tile_s[1] = 1
tile_s[2] = 2

for i in range(3, N+1):
    tile_s[i] = (tile_s[i-1] + tile_s[i-2])%15746

print(tile_s[N])