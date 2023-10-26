# 금광문제
# n*m크기
# 채굴자가 얻을 수 있는 금의 최대 크기
# 오른쪽 ,오른쪽 위,오른쪽 아래 움직있을 수 있음
# 왼쪽 위,왼쪽,왼쪽아래에서 오는 경우
# 세가지 경우중 가장 큰 값
# array[i][j]=i 행 j열에 존재하는 금의양
# dp[i][j]=i행 j열까지의 최적의 해(얻을 수 있는 금의 최댓값)
# 점화식 d[i][j]=array[i][j]+max(dp[i-1][i-1],dp[i][j-1],dp[i+1][j-1])

# 테스트 케이스 입력
for tc in range(int(input())):
    # 금광정보 입력
    n, m = map(int, input().split())
    array = list(map(int, input().split()))
    # 다이나믹 프로그래밍을 위한 2차원 DP테이블 초기화
    dp = []
    index = 0
    for i in range(n):
        # m 단위로 슬라이싱해서 2차원 배열로 만든다
        dp.append(array[index:index+m])
        index += m
    for j in range(1, m):
        for i in range(n):
            # 왼쪽 위에서 오는 경우
            if i == 0:
                left_up = 0
            else:
                left_up = dp[i-1][j-1]
            # 왼쪽 아래에서 오는 경유
            if i == n-1:
                left_down = 0
            else:
                left_down = dp[i+1][j-1]
            # 왼쪽에서 오는 경유
            left = dp[i][j-1]
            dp[i][j] = dp[i][j]+max(left_down, left, left_up)
    result = 0
    for i in range(n):
        result = max(result, dp[i][m-1])
    print(result)
