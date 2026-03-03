import sys

n = int(sys.stdin.readline().rstrip())
m = int(sys.stdin.readline().rstrip())

data = list(map(int, sys.stdin.readline().split()))

# [학생 번호, 추천 수, 게시 시각]
board = []
time = 0

# 학생 리스트 순회
for d in data:
    time += 1
    found = False
    
    # 이미 게시된 학생이면 추천수만 증가
    for b in board:
        if b[0] == d:
            found = True
            b[1] += 1
            break
    if found:
        continue
    # 아직 게시판이 꽉차지 않았다면
    if found == False and len(board) < n:
        board.append([d, 1, time])
        found = True
        continue
        
    # 게시판이 꽉차서 하나를 지워야 하는 상황이면 => 추천수, 먼저 게시된순
    board.sort(key = lambda x : (x[1], x[2]))
    board.pop(0)
    board.append([d, 1, time])
    found = True
ans = []
for i in range(len(board)):
    ans.append(board[i][0])
ans.sort()
print(*ans)