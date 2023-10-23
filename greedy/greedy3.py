# 곱하기 혹은 더하기 문제
# 연산잔를 이용하여 만들 수 있는 가장 큰 수 만들기
data=input()
result=int(data[0])
#1번 인데스 부터 시작하는 이유는 초기 result에 0번째 인덱스에 있는 값을 넣어 주었기 때문이다
for i in range(1,len(data)):
    num=int(data[i])
    if num<=1 or result <=1:
        result +=num
    else:
        result*=num

print(result)
 