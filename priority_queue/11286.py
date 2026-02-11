import sys
import heapq

n = int(sys.stdin.readline().strip())
q = []
for _ in range(n):
    order = int(sys.stdin.readline().strip())
    if order == 0:
        if len(q) == 0:
            print(0)
            continue
        else:
            a = heapq.heappop(q)
            print(a[1])
            continue
    else:
        heapq.heappush(q,(abs(order), order))
        