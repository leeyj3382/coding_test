s = input()

nums = {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9'}
num_result = 0
num_count = 0
string_result = []

for data in s:
	if data in nums :
		num_result += int(data)
		num_count += 1
	else :
		string_result.append(data)

if num_count > 0 :
	if len(string_result) > 0:
		string_result.sort()
		for i in string_result:
			print(i, end='')
	print(num_result)
else :
	string_result.sort()
	for i in range(len(string_result)-1):
		print(i, end='')
	print(string_result[-1])