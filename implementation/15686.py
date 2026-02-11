import sys
from itertools import combinations

INF = int(1e9)
n, m = map(int, sys.stdin.readline().split())

chicken = []
house = []
for i in range(n):
    tmp = list(map(int, sys.stdin.readline().split()))
    for j in range(n):
        if tmp[j] == 1:
            house.append((i, j))
        elif tmp[j] == 2:
            chicken.append((i, j))
            
ans = INF
for comb in combinations(chicken, m):
    city_dist = 0
    for hx, hy in house:
        best = INF
        for cx, cy in comb:
            d = abs(hx - cx) + abs(hy - cy)
            if d < best:
                best = d
        city_dist += best
    if city_dist < ans:
        ans = city_dist
    
print(ans)