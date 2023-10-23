n,k=map(int,input().split())
friends=[]
for _ in range(n):
    friends.append(int(input()))
diff=[]
for i in range(friends.__len__()-1):
    diff.append(friends[i+1]-friends[i]) #친구들의 방문 시간차 
diff.sort()# 오름차순 정렬

for _ in range(k-1):
    diff.pop()#거리가 긴 구간 부터 잘라준다

for _ in range(k):
    diff.append(1) # -1이 k 만큼 되었으므로 마지막에 +1씩 해준다
    
print(sum(diff))
print(diff)

# 그리디 +문제  2212번 13614번 비슷한 문제
# 일렬로 나타날때 사이의 거리 및 시간