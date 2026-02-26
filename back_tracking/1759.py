import sys

l, c = map(int, sys.stdin.readline().split())

data = list(map(str, sys.stdin.readline().split()))
data.sort()
v = ['a', 'e', 'i', 'o', 'u']

def dfs(start, crypt, v_cnt, c_cnt):
    if len(crypt) == l:
        if v_cnt >= 1 and c_cnt >= 2:
            print(''.join(crypt))
            return
    for i in range(start, c):
        ch = data[i]
        crypt.append(ch)
        if ch in v:
            dfs(i+1, crypt, v_cnt +1, c_cnt)
        else:
            dfs(i+1, crypt, v_cnt, c_cnt+1)
        crypt.pop()

dfs(0, [], 0, 0)