import sys

n = int(sys.stdin.readline().strip())
col = []
for i in range(n):
    col.append(list(map(int, sys.stdin.readline().split())))
col.sort()

max_h = 0
max_idx = 0

for i,(x, h) in enumerate(col):
    if max_h < h:
        max_h = h
        max_idx = i

# 가장 큰 기둥 기준으로 왼쪽, 오른쪽 나눠서
total = 0

cur_col = col[0][1]
for i in range(max_idx):
    x1, h1 = col[i]
    x2, h2 = col[i+1]
    cur_col = max(cur_col, h1)
    total += cur_col * (x2 - x1)

cur_col = col[-1][1]
for i in range(n-1, max_idx, -1):
    x1, h1 = col[i]
    x2, h2 = col[i-1]
    cur_col = max(cur_col, h1)
    total += cur_col * (x1 - x2)
    
total += max_h

print (total)


