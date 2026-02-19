import sys

gear = []
for _ in range(4):
    gear.append(list(map(int, sys.stdin.readline().strip())))
    
k = int(sys.stdin.readline().strip())
# 시계방향 회전
def right(num):
    tmp = gear[num][7]
    gear[num][7] = gear[num][6]
    gear[num][6] = gear[num][5]
    gear[num][5] = gear[num][4]
    gear[num][4] = gear[num][3]
    gear[num][3] = gear[num][2]
    gear[num][2] = gear[num][1]
    gear[num][1] = gear[num][0]
    gear[num][0] = tmp
# 반시계 방향 회전
def left(num):
    tmp = gear[num][0]
    gear[num][0] = gear[num][1]
    gear[num][1] = gear[num][2]
    gear[num][2] = gear[num][3]
    gear[num][3] = gear[num][4]
    gear[num][4] = gear[num][5]
    gear[num][5] = gear[num][6]
    gear[num][6] = gear[num][7]
    gear[num][7] = tmp
    
for i in range(k):
    target, d = map(int, sys.stdin.readline().split())
    target -= 1
    l = target - 1
    r = target + 1
    rotate = [0,0,0,0]
    rotate[target] = d
    # 왼쪽 확인(첫번째 기어면 패스)
    while l >= 0:
        if gear[l][2] != gear[l+1][6]:
            rotate[l] = -rotate[l+1]
            l -= 1
        # 같은 극이면 전파 중단
        else:
            break
    # 오른쪽
    while r < 4:
        if gear[r][6] != gear[r-1][2]:
            rotate[r] = -rotate[r-1]
            r += 1
        else:
            break
            
    for j in range(4):
        if rotate[j] == 1:
            right(j)
        elif rotate[j] == -1:
            left(j)
print(gear[0][0]*1 + gear[1][0]*2 + gear[2][0]*4 + gear[3][0]*8)     