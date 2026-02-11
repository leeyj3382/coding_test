import sys
import heapq

t = int(sys.stdin.readline().strip())
for tc in range(t):
    k = int(sys.stdin.readline().strip())
    max_h = []
    min_h = []
    alive = [False] * k
    
    for i in range(k):
        op, x = map(str, sys.stdin.readline().split())
        x = int(x)
        
        if op == "I":
            heapq.heappush(max_h, (-x, i))
            heapq.heappush(min_h, (x, i))
            alive[i] = True
        # op = 'D'    
        else:
            # max_h
            if x == 1:
                # 큐가 비어있지 않고, 큐 최상단 값이 죽어 있으면 버리고 다시 뽑기
                while max_h and not alive[max_h[0][1]]:
                    heapq.heappop(max_h)
                # 큐 최상단 값이 살아있으면 탈출
                # 큐가 비어있지 않으면
                if max_h:
                    _, idx = heapq.heappop(max_h)
                    alive[idx] = False
            else:
                while min_h and not alive[min_h[0][1]]:
                    heapq.heappop(min_h)
                if min_h:
                    _,idx = heapq.heappop(min_h)
                    alive[idx] = False
    # 반영되지 않은 녀석들 정리
    while max_h and not alive[max_h[0][1]]:
        heapq.heappop(max_h)
    while min_h and not alive[min_h[0][1]]:
        heapq.heappop(min_h)
        
    if not min_h or not max_h:
        print("EMPTY")
    else:
        print(-max_h[0][0], min_h[0][0])