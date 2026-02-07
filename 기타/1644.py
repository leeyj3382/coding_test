import sys
import math

n = int(sys.stdin.readline())
table = [0]
for i in range(1, n+1):
    table.append(i)
# 소수 판별 : 에라토스테네스의 체    
for i in range(2, int(math.sqrt(n))+1):
    j = 2
    # 소수의 배수(소수가 아님) 지우기
    while i * j <= n:
        table[i*j] = 0
        j += 1

prime_table = []
for a in table:
    if a != 0 and a!= 1:
        prime_table.append(a)

count = 0
end = 0
interval_sum = 0
for start in range(len(prime_table)):
    while interval_sum < n and end < len(prime_table):
        interval_sum += prime_table[end]
        end += 1
    # 만약 찾으면
    if interval_sum == n:
        count += 1
    interval_sum -= prime_table[start]
print(count)