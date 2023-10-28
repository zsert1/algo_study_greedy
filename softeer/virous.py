
# 초기화
# 1초당 P배증가
# 묘듈러 연산 사용
# 덧셈 : (a+b) % M = ((a % M) + (b % M)) % M
# 뺄셈 : (a-b) % M = ((a%M) - (a%M)) % M
# 곱셈 : (a*b) % M = ((a*M) * (b*M)) % M

k, p, n = map(int, input().split())

# 초기화 1번째 바이러스 수
result = k
for i in range(n):
    # result에 값에 따라 변경
    a = result % 1000000007
    b = p % 1000000007
    # result 값 n에 따라 변경(2->6->18)
    result = (a * b) % 1000000007

print(result)
