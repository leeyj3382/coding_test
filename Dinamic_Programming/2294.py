n, k = map(int, input().split())

# 입력받은 화폐 종류
a = list(int(input()) for _ in range(n))

# k원까지의 dp 테이블(만들 수 없는 경우를 디폴트)
d = [10001 for _ in range (k+1)]


d[0] = 0
for coin in a:
    for i in range(coin, k+1):
        d[i] = min(d[i], d[i-coin] + 1)
        
print(d[k] if d[k]!= 10001 else -1)