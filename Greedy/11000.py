import sys
import heapq

n = int(sys.stdin.readline().strip())

lec = []
for i in range(n):
    s, e = map(int, sys.stdin.readline().split())
    lec.append((s, e))
lec.sort()

room = []
for s, e in lec:
    if room and room[0] <= s:
        heapq.heappop(room)
    heapq.heappush(room, e)
    
print(len(room))
        