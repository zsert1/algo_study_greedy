# 바이러스 문제
K, P, N = map(int, input().split())
result = K
for n in range(N):
    a = result % 1000000007
    b = a % 1000000007
    result = (a*b) % 1000000007
print(result)
