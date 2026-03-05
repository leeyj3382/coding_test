def solution(s):
    n = len(s)
    if n == 1:
        return 1
    ans = n
    
    for w in range(1, n//2 + 1):
        prev = s[0:w]
        cnt = 1
        compressed = []
        for i in range(w, n, w):
            cur = s[i:i+w]
            if cur == prev:
                cnt += 1
            else:
                if cnt == 1:
                    compressed.append(prev)
                else:
                    compressed.append(str(cnt) + prev)
                prev = cur
                cnt = 1
        if cnt == 1:
            compressed.append(prev)
        else:
            compressed.append(str(cnt) + prev)
        ans = min(ans, len(''.join(compressed)))
    return ans