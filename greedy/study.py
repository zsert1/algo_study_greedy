n = int(input())
coins = [500, 100, 50, 10, 5, 1]
money = 1000-n
result = 0
for coin in coins:
    if coin <= money:
        result += money//coin
        money %= coin
print(result)
