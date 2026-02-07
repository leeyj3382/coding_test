import sys

n, m = map(int, sys.stdin.readline().split())

parent = [0] * (n+1)
for i in range(1, n+1):
    parent[i] = i
    
games = []

def find_parent(parent,x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else :
        parent[a] = b

# 일단 게임 내역들 다 저장
for i in range(m):
    a, b = map(int, sys.stdin.readline().split())
    games.append((a,b))

result = 0
turn = 1
for game in games:
    a, b = game
    if find_parent(parent, a) == find_parent(parent, b):
        result = turn
        break
    else:
        union_parent(parent, a, b)
        turn += 1
print(result)