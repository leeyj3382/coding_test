import sys

n, m = map(int, sys.stdin.readline().split())
parent = [0]*(n+1)
for i in range(1, n+1):
    parent[i] = i
    
def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]
def union(a, b):
    a = find(a)
    b = find(b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

known = list(map(int, sys.stdin.readline().split()))
known_person = known[1:]
for i in range(len(known_person)-1):
    union(known_person[i], known_person[i+1])

party = []
for _ in range(m):
    tmp = list(map(int, sys.stdin.readline().split()))
    people = tmp[1:]
    party.append(people)
    for i in range(len(people)-1):
        union(people[i], people[i+1])
        
known_roots = set(find(x) for x in known_person)

count = 0
for pa in party:
    can_lie = True
    for p in pa:
        if find(p) in known_roots:
            can_lie = False
            break
    if can_lie:
        count += 1
        
print(count)