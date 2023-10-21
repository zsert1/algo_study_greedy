# 유치원 문제
n,k=map(int,input().split())
childern=list(map(int,input().split() ))

diff=[]
for i in range(childern.__len__()-1):
    diff.append(childern[i+1]-childern[i])
diff.sort()
for _ in range(k-1):
    diff.pop()

print(sum(diff))



