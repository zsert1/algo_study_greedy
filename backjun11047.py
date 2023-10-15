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