n,k=map(int,input().split())
coins=[]
#화폐의 종류 만큼 생성
for s in range(n):
    coins.append(int(input()))
# 오름차순으로 정리 최솟값이기 때문에
coins.sort(reverse=True)

answer=0
for coin in coins:
    if(k>=coin):
        answer+=k//coin
        k%=coin
        if(k<=0):
            break
print(answer)

## 생각할 것 int형으로 입력받기
## 화폐의 종류만큼 코인을 입력 받는다
## 코인을 오름차순으로 정렬
## //을 사용하여 몫을 구한다.
## 나머지를 k에 넣어주어 0보다 작아질 떄 까지 반복한다(나머지가 존재하지 않을떄 까지)  