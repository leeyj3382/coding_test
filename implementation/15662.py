import sys

n = int(sys.stdin.readline().strip())

gear = []
for i in range(n):
    gear.append(list(map(int, sys.stdin.readline().strip())))
    
def right(num):
    tmp = gear[num][-1]
    for i in range(7, 0, -1):
        gear[num][i] = gear[num][i-1]
    gear[num][0] = tmp
    
def left(num):
    tmp = gear[num][0]
    for i in range(7):
        gear[num][i] = gear[num][i+1]
    gear[num][-1] = tmp
    
k = int(sys.stdin.readline().strip())
order = []
for i in range(k):
    order.append(list(map(int, sys.stdin.readline().split())))

for o in order:
    idx, d = o
    idx -= 1
    
    l = idx - 1
    r = idx + 1
    rotate = [0] * n
    rotate[idx] = d
    
    while l >= 0:
        if gear[l][2] != gear[l+1][6]:
            rotate[l] = -rotate[l+1]
            l -= 1
        else:
            break
            
    while r < n:
        if gear[r][6] != gear[r-1][2]:
            rotate[r] = -rotate[r-1]
            r += 1
        else:
            break
    
    for i in range(n):
        if rotate[i] == 1:
            right(i)
        elif rotate[i] == -1:
            left(i)

count = 0
for i in range(n):
    if gear[i][0] == 1:
        count += 1
        continue
print(count)
