n = int(input())

a = []
for i in range(n):
	a.append(int(input()))

    
d = []
# d[i번째 잔][지금까지 포함해서 연속으로 마신 수(이번에 안 마셨으면 0으로 초기화)]
# -1 : 불가능한 경우의 수
for i in range(n):
    d.append(list(-1 for i in range(3)))

# n이 2보다 작거나 같으면 합해서 출력 및 조기종료
if n <= 2:
    print(sum(a))
    exit()
    
d[0][0] = 0
d[0][1] = a[0]
d[1][0] = d[0][1]
d[1][1] = d[0][0] + a[1]
d[1][2] = d[0][1] + a[1]

for i in range(2, n):
    d[i][0] = max(d[i-1][0], d[i-1][1], d[i-1][2])
    d[i][1] = d[i-1][0] + a[i]
    d[i][2] = d[i-1][1] + a[i]

print(max(d[n-1][0], d[n-1][1], d[n-1][2]))