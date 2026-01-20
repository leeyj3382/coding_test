n = int(input())
party = list(map(int, input().split()))

num_group = 0
max = -1
party_tmp = []

for human in party :
	party_tmp.append(human)
	if max < human :
		max = human
	if max >= len(party_tmp):
		party_tmp = []
		max = -1
		num_group += 1

print(num_group)