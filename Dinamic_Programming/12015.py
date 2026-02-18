import sys
from bisect import bisect_left

n = int(sys.stdin.readline().strip())
data = list(map(int, sys.stdin.readline().split()))

lis = []

for x in data:
    pos = bisect_left(lis, x)
    if len(lis) == pos:
        lis.append(x)
    else:
        lis[pos] = x
        
print(len(lis))
