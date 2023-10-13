## 모험가 길드
# 최대한 많은 그룹수 만들기
# 오름 차순 정렬 이후에 가장 작은 값 부터 정렬
n= int(input())
data=list(map(int,input().split()))
data.sort() #오름차순
print(data)
result=0
count=0
for i in data:
    count+=i
    if count>=n:
        result+=1
        count=0
print(result)