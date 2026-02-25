import sys

n = int(sys.stdin.readline().strip())

minus = []
zero = 0
one = 0
large = []

for i in range(n):
    tmp = int(sys.stdin.readline().strip())
    if tmp > 1 :
        large.append(tmp)
    elif tmp < 0 :
        minus.append(tmp)
    elif tmp == 0:
        zero += 1
    else:
        one += 1

if len(minus) > 1:
    minus.sort()
if len(large) > 1:
    large.sort(reverse = True)
    

def cal(zero, one):
    result = 0
    # 음수가 있다면
    if len(minus) > 0:
        # 홀수개라면
        if len(minus) % 2 == 1:
            # 만약 하나라면
            if len(minus) == 1:
                # 여분의 0이 있다면
                if zero > 0:
                    zero -= 1
                else:
                    result += minus[0]
            # 만약 하나가 아닌 홀수라면
            else :
                # 마지막 하나가 남을 때까지 곱해서 더하기
                for i in range(0,len(minus)-2,2):
                    result += (minus[i] * minus[i+1])
                # 0 남아 있으면 마지막 녀석은 없애기
                if zero > 0:
                    zero -= 1
                else:
                    result += minus[0]
        # 짝수개라면
        else :
            # 앞에 애들부터 곱해서 더하기
            for i in range(0,len(minus)-1,2):
                result += (minus[i] * minus[i+1])
    # 2 이상의 값이 있다면
    if len(large) > 0:
        # 홀수개라면
        if len(large) % 2 == 1:
            # 하나라면
            if len(large) == 1:
                result += large[0]
            # 하나가 아닌 홀수개라면
            else: 
                for i in range(0,len(large)-2,2):
                    result += (large[i] * large[i+1])
                result += large[0]
        # 짝수개라면
        else:
            for i in range(0,len(large)-1,2):
                result += (large[i] * large[i+1])
    # 1은 개수만큼 더해주기
    result += one
    return result

ans = cal(zero, one)
print(ans)