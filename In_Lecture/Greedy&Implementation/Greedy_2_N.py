import sys
S = sys.stdin.readline().rstrip()

result = int(S[0])

for i in range(1,len(S)):
	n = int(S[i])
	if result < 2 or n < 2:
		result += n
	else :
		result *= n

print(result)
	