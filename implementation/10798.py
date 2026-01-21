import sys

data = []
result = []

for i in range(5):
	s = sys.stdin.readline().rstrip()
	data.append(s)

for i in range(15):
	for j in range(5):
		if len(data[j])-1 < i:
			continue
		result.append(data[j][i])

print("".join(result))