import sys
from collections import deque

t = int(sys.stdin.readline().strip())

for tc in range(t):
    order = list(map(str, sys.stdin.readline().strip()))
    n = int(sys.stdin.readline().strip())
    
    tmp_line = sys.stdin.readline().strip()
    if n == 0:
        board = deque()
    else:
        board= deque(map(int,tmp_line[1:-1].split(',')))
    
    reverse = False
    error = False
    for o in order:
        if o == 'D':
            if len(board) <= 0:
                error = True
                break
            if not reverse:
                board.popleft()
            elif reverse:
                board.pop()
        elif o == 'R':
            if not reverse:
                reverse = True
            elif reverse:
                reverse = False
    if error == True:
        print('error')
    else:
        if reverse:
            board.reverse()
        print("[" + ",".join(map(str, board)) + "]")