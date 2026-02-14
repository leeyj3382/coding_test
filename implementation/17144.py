import sys

r, c, t = map(int, sys.stdin.readline().split())
board = []
clean = []
for i in range(r):
    row = list(map(int, sys.stdin.readline().split()))
    board.append(row)
    if row[0] == -1:
        clean.append(i)

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def spread():
    # 임시 배열. 나중에 board에 더할 예정
    # 이 배열이 있기 때문에, 언제 확산 되었는지를 추적하지 않아도 됨
    add = [[0] * c for _ in range(r)]
    for x in range(r):
        for y in range(c):
            # 만약 먼지가 있는 칸이면
            if board[x][y] > 0 :
                amount = board[x][y] // 5
                if amount == 0:
                    continue
                cnt = 0
                for k in range(4):
                    nx = x + dx[k]
                    ny = y + dy[k]
                    if nx < 0 or nx >= r or ny < 0 or ny >= c:
                        continue
                    if board[nx][ny] == -1:
                        continue
                    add[nx][ny] += amount
                    cnt += 1
                board[x][y] -= amount * cnt
    # add 리스트를 더해줌 => board 최신화
    # lazy update 그런건가
    for x in range(r):
        for y in range(c):
            board[x][y] += add[x][y]
            
def purify():
    # 위쪽, 아래쪽 공청기
    upper = clean[0]
    lower = clean[1]
    
    # 위쪽 - 반시계
    for x in range(upper-1, 0, -1):# 왼쪽
        board[x][0] = board[x-1][0]
    for y in range(0, c-1):# 위쪽
        board[0][y] = board[0][y+1]
    for x in range(0, upper):# 오른쪽
        board[x][c-1] = board[x+1][c-1]
    for y in range(c-1, 1, -1):# 아래쪽
        board[upper][y] = board[upper][y-1]
    board[upper][1]=0
        
    # 아래쪽 - 시계
    for x in range(lower+1, r-1): # 왼쪽
        board[x][0] = board[x+1][0]
    for y in range(0, c-1): # 아래
        board[r-1][y] = board[r-1][y+1]
    for x in range(r-1, lower, -1):# 오른쪽
        board[x][c-1] = board[x-1][c-1]
    for y in range(c-1, 1, -1):
        board[lower][y] = board[lower][y-1]
    board[lower][1] = 0

for _ in range(t):
    spread()
    purify()
ans = 0
for i in range(r):
    for j in range(c):
        if board[i][j] > 0:
            ans += board[i][j]
print(ans)