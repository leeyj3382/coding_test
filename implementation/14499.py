import sys

n, m, x, y, k = map(int, sys.stdin.readline().split())

board = []
for _ in range(n):
    board.append(list(map(int, sys.stdin.readline().split())))
order = list(map(int, sys.stdin.readline().split()))

# 0=top, 1=bottom, 2=north, 3=south, 4=east, 5=west
dice = [0, 0, 0, 0, 0, 0]
# 0, 동, 서, 북, 남
dx = [0, 0, 0, -1, 1]
dy = [0, 1, -1, 0, 0]

for o in order:
    nx = x + dx[o]
    ny = y + dy[o]
    if nx < 0 or nx >= n or ny < 0 or ny >= m:
        continue
    
    top, bottom, north, south, east, west = dice
    # 동쪽으로 굴렸을 때
    if o == 1:
        dice[0] = west
        dice[1] = east
        dice[2] = north
        dice[3] = south
        dice[4] = top
        dice[5] = bottom
    # 서쪽
    elif o == 2:
        dice[0] = east
        dice[1] = west
        dice[2] = north
        dice[3] = south
        dice[4] = bottom
        dice[5] = top
    elif o == 3:
        dice[0] = south
        dice[1] = north
        dice[2] = top
        dice[3] = bottom
        dice[4] = east
        dice[5] = west
    elif o == 4:
        dice[0] = north
        dice[1] = south
        dice[2] = bottom
        dice[3] = top
        dice[4] = east
        dice[5] = west
        
    x, y = nx, ny
    if board[x][y] == 0:
        board[x][y] = dice[1]
    else :
        dice[1] = board[x][y]
        board[x][y] = 0
        
    print(dice[0])
        