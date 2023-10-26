# 병사배치
# 전투력이 높은 병사가 앞쪽에 오도록
# 가장 긴 증가하는 부분 수열
# 가장 긴 감소하는 부분 수열
# 점화식
# 부분 수열 최대 길이
# 모든 0<=j<i 에 대하여, D[i]=max(D[i],D[j]+1) if array[j]< array[i]
n = int(input())
array = list(map(int, input().split()))
array.reverse()

dp = [1]*n

for i in range(1, n):
    for j in range(0, i):
        if array[j] < array[i]:
            dp[i] = max(dp[i], dp[j]+1)
print(n-max(dp))
