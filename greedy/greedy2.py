## 1이 될 떄 까지 문제
## n,k를 공백기준으로 구분하여 입력받기
n,k=map(int,input().split())
result=0
while True:
    target=(n//k)*k
    result+=(n-target)
    n=target
    if n<k:
        break
    result+=1
    n//=k

result+=n-1
print(result)