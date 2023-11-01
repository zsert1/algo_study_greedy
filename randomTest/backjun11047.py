# 동전 0으로 만들기
N, M = map(int, input().split())
coins = [int(input()) for _ in range(N)]
# 최솟 값이므로 오름차순정렬
coins.sort(reverse=True)
result = 0
for coin in coins:
    if M-coin >= 0:
        result += M//coin
        M %= coin

print(result)
