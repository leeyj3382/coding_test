data = input()
result = []
value = 0
has_digit = False

# 문자를 하나씩 확인하며
for x in data:
	
	# 알파벳인 경우 결과 리스트에 삽입
	if x.isalpha():
		result.append(x)
	# 숫자는 따로 더하기
	else:
		value += int(x)
		# 플래그 바꿔주기
		has_digit = True

result.sort()

# 플래그 기준으로 분기
if has_digit:
	result.append(str(value))
	

print(''.join(result))