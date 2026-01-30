n, k = map(int, input().split())

items = []
for _ in range(n):
	w, v = map(int, input().split())
	items.append((w, v))
	
dp = [0] * (k+1)

for w, v in items :
	for cap in range(k, w-1, -1):
		dp[cap] = max(dp[cap], dp[cap-w]+v)
		
print(dp[k])