N,L=map(int,input().split())
h=list(map(int,input().split()))
h.sort()

for _ in h:
    if(_<=L):
        L+=1
    else:
        L=L

print(L)
        
## 생각할 것 int형으로 입력받기
## 과일을 오름차순으로 정렬
 