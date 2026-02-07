import sys
from collections import deque

n = int(sys.stdin.readline())

# 작업 리스트
works = [[] for i in range(n+1)]
# 각 작업의 소요시간
times = [0] * (n+1)
# 진입차수
indegree = [0] * (n+1)

# 작업 정보 업데이트 => 작업별 소요시간, 선행관계, 진입차수
for i in range(1, n+1):
    tmp = list(map(int, sys.stdin.readline().split()))
    k = tmp[1]
    times[i] = tmp[0]
    for j in range(2, 2+k):
        works[tmp[j]].append(i)
        indegree[i] += 1
# 최소 작업시간을 기록할 dp테이블
dp = [0] * (n+1)

def topology_sort():
    q = deque()
    for i in range(1, n+1):
        # 기본값
        dp[i] = times[i]
        # 바로 시작해도 되는 작업들
        if indegree[i] == 0:
            q.append(i)
    while q:
        now = q.popleft()
        for nxt in works[now]:
            dp[nxt] = max(dp[nxt], dp[now] + times[nxt])
            indegree[nxt] -= 1
            if indegree[nxt] == 0:
                q.append(nxt)
                
topology_sort()  
print(max(dp))