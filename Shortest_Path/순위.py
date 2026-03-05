# 방향이 있는 그래프
# 도달이 가능한 지점을 찾는 문제
# 선수 최대가 100명 => O(N**3) = 1000000
# 플로이드 워셜

def solution(n, results):
    
    INF = int(1e9)
    
    board = [[INF] * (n+1) for _ in range(n+1)]
    
    for a in range(1, n+1):
        for b in range(1, n+1):
            if a == b:
                board[a][b] = 0
    
    for i in range(len(results)):
        a, b = results[i]
        board[a][b] = 1
    
    for k in range(1, n+1):
        for a in range(1, n+1):
            for b in range(1, n+1):
                board[a][b] = min(board[a][b], board[a][k] + board[k][b])
    ans = 0
    for a in range(1, n+1):
        known = 0
        for b in range(1, n+1):
            if a == b:
                continue
            if board[a][b] != INF or board[b][a] != INF:
                known += 1
        if known == n-1:
            ans += 1
                
    return ans