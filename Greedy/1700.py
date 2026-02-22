import sys

n, k = map(int, sys.stdin.readline().split())
work = list(map(int, sys.stdin.readline().split()))

tap = []

def find_target(cur):
    remove = -1
    farthest = -1
    for j in range(len(tap)):
        a = tap[j]
        used = False
        next_use = -1
        for i in range(cur, k):
            if a == work[i]:
                # i번째에서 다시 쓰임
                next_use = i
                used = True
                break
        # 현재 텝에서 다시 쓰이지 않는 녀석이 있다면 먼저 제거        
        if not used:
            return j
        if  farthest < next_use:
            farthest = next_use
            remove = j

    # 현재 텝에서 다음에 가장 늦게 다시 사용되는 녀석을 제거
    return remove 

result = 0
for i in range(k):
    # 이미 있으면
    if work[i] in tap:
        continue
    # 비어있으면 꽂기
    if len(tap) < n:
        tap.append(work[i])
        continue
    tmp = find_target(i)
    tap[tmp] = work[i]
    result += 1
print(result) 
    