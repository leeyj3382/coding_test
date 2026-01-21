n = input()

count = [ 0 for i in range(10) ]

for num in n:
	count[int(num)] += 1

if (count[6] + count[9])%2 == 0 :
	count[6] = (count[6] + count[9])//2
	count[9] = 0
else :
	count[6] = (count[6] + count[9])//2 + 1
	count[9] = 0
	
print(max(count))