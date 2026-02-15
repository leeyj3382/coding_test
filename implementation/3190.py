import sys
from collections import deque
n = int(sys.stdin.readline().strip())
snake = deque()
board = [[0]*(n) for _ in range(n)]
dx = [0, -1, 1, 0, 0]
dy = [0, 0, 0, -1, 1]
board[0][0] = 4
snake.append((0,0))

# 사과 개수
k = int(sys.stdin.readline().strip())
# 사과 위치 마킹
for _ in range(k):
    x, y = map(int, sys.stdin.readline().split())
    board[x-1][y-1] = -1
# 방향 전환 명령 기록    
l = int(sys.stdin.readline().strip())
order = []
for _ in range(l):
    x, d = map(str, sys.stdin.readline().split())
    x = int(x)
    order.append((x, d))

def move():
    x, y = snake[-1]
    d = board[x][y]
    nx = x + dx[d]
    ny = y + dy[d]
    # 벽에 닿으면
    if nx < 0 or nx >= n or ny < 0 or ny >= n:
        return False
    # 본인 몸에 닿으면
    if board[nx][ny] > 0:
        return False
    # 사과가 있으면
    if board[nx][ny] == -1:
        board[nx][ny] = d
        snake.append((nx,ny))
    # 사과가 없으면
    else:
        board[nx][ny] = d
        snake.append((nx,ny))
        tail = snake[0]
        board[tail[0]][tail[1]] = 0
        snake.popleft()
        
    return True

def turn(o):
    head = snake[-1]
    x, y = head
    d = board[x][y]
    # 오른쪽으로 틀기
    if o == 'D':
        # 1-상 2-하 3-좌 4-우
        if d == 1:
            d = 4
        elif d == 2:
            d = 3
        elif d == 3:
            d = 1
        else:
            d = 2
    elif o == 'L':
        if d == 1:
            d = 3
        elif d == 2:
            d = 4
        elif d == 3:
            d = 2
        else:
            d = 1
    board[x][y] = d

crash = True
t = 0
order_pointer = 0
while crash:
    crash = move()
    t += 1
    if order_pointer < l and t == order[order_pointer][0]:
        turn(order[order_pointer][1])
        order_pointer += 1

print(t)
    