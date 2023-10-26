# 효울적 화폐구성
# step 0(초기화)
# 각화폐의 종류를 하나씩 늘려가며 확인해야 한다
# N개의 화폐단위
# M은 만들 돈
N, M = map(int, input().split())
array = []
for i in range(N):
    array.append(int(input()))
d = [10001]*(M+1)
# i는 각각의 화폐단위
# 보텀업 문제
for i in range(N):
    # j는 각각의 금액
    for j in range(array[i], M+1):
        if d[j-array[i]] != 10001:  # (i-k)원을 만드는 방법이 존재하는 경우
            d[j] = min(d[j], d[j-array[i]]+1)

if d[M] == 10001:
    print(-1)
else:
    print(d[M])
