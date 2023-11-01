# 지도 구축
# 2,3,5,7
# 0,1,2,3
# 점의 갯수에 따른 점화식 구성
n = int(input())
dp = [0]*16
dp[0] = 2
for i in range(1, n+1):
    dp[i] = dp[i-1]+2**(i-1)
