import sys

n = int(sys.stdin.readline())

meetings = []

# O(N)
# [start, end] 꼴로 저장
for i in range(n):
	meetings.append(list(map(int, sys.stdin.readline().split())))

# 회의가 '끝나는' 시간을 기준으로 정렬
meetings.sort(key = lambda x : (x[1], x[0]))

count = 0
latest_meeting_start = 0
latest_meeting_end = 0


for s, e in meetings :
	# 그럼 조건이 => 선택된 미팅의 시작 시간이 이전 회의의 시작시간과 끝 시간에 걸치면 안되고
	# 선택된 미팅의 끝나는 시간이 이전 회의의 시작시간과 끝 시간에 걸치면 안되는 거니까.
	# 그냥 이전 회의가 끝난 이후면 되겠네(인풋이 정상적이니까)
	if latest_meeting_end > s :
		continue
	count += 1
	latest_meeting_start = s
	latest_meeting_end = e

print(count)