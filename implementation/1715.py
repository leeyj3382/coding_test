import sys
import heapq

n = int(sys.stdin.readline().strip())

data = []
for i in range(n):
    data.append(int(sys.stdin.readline().strip()))
if len(data)<=2:
    print(sum(data))
    exit()
    
q = []
    
for a in data:
    heapq.heappush(q, a)


while q:
    # 제일 작은 두 녀석 뽑고
    first = heapq.heappop(q)
    if len(q) == 0:
        print(first)
        exit()
    second = heapq.heappop(q)
    tmp = first + second
    # 더한 값을 다시 우선순위 큐에 넣음
    heapq.heappush(q, tmp)
    