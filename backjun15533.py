n,k=map(int,input().split())
friends=[]
for _ in range(n):
    friends.append(int(input()))
diff=[]
for i in range(friends.__len__()-1):
    diff.append(friends[i+1]-friends[i])
diff.sort()

for _ in range(k-1):
    diff.pop()
for _ in range(k):
    diff.append(1)
print(sum(diff))

# 그리디 +문제  2212번 13614번 비슷한 문제