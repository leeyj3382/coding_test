import sys

n = int(sys.stdin.readline())

parent = [0] * (n+1)
for i in range(1, n+1):
    parent[i] = i

edges = []
result = 0
for i in range(1, n+1):
    tmp = list(map(int, sys.stdin.readline().split()))
    for j in range(len(tmp)):
        # i에서 j 간선 유지 비용 tmp[j]
        edges.append((tmp[j], i, j+1))
# 루트 찾기        
def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]
# 합집합
def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b
# 크루스칼 알고리즘 쓰기 위한 정렬
edges.sort()

for edge in edges:
    cost, a, b = edge
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        result += cost
        
print(result)