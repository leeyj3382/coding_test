n = int(input())

distance_data = list(map(int, input().split()))
price_data = list(map(int, input().split()))

payment = 0
i, j = 0, 1

while (j < n):
	
	if price_data[i] > price_data[j]:
		payment += distance_data[j-1] * price_data[i]
		i = j
		j += 1
	else :
		payment += distance_data[j-1] * price_data[i]
		j += 1

print(payment)