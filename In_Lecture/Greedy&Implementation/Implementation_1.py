n = int(input())

hour = 0
minute = 0
sec = 0
count = 0

while (hour != n or minute != 59 or sec != 59):
	# 3 있나 확인
	if((str(hour).count('3') > 0 or str(minute).count('3') > 0 or str(sec).count('3') > 0)):
		count += 1
	

	# 증감식
	sec += 1
	
	# 시간 조정
	if(sec == 60):
		sec = 0
		minute += 1
	if(minute == 60):
		minute = 0
		hour += 1
		
print(count)