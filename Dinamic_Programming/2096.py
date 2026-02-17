import sys

n = int(sys.stdin.readline().strip())

a, b, c = map(int, sys.stdin.readline().split())

max_prev = [a, b, c]
min_prev = [a, b, c]

for i in range(n-1):
    a, b, c = map(int, sys.stdin.readline().split())
    cur_max0 = max(max_prev[0], max_prev[1]) + a
    cur_max1 = max(max_prev[0], max_prev[1], max_prev[2]) + b
    cur_max2 = max(max_prev[1], max_prev[2]) + c
    
    cur_min0 = min(min_prev[0], min_prev[1]) + a
    cur_min1 = min(min_prev[0], min_prev[1], min_prev[2]) + b
    cur_min2 = min(min_prev[1], min_prev[2]) + c
    
    max_prev = [cur_max0, cur_max1, cur_max2]
    min_prev = [cur_min0, cur_min1, cur_min2]
    
print(max(max_prev), min(min_prev))