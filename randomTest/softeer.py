# 금고 털이
# greedy로 푼다
W, N = map(int, input().split())
list = [list(map(int, input().split())) for _ in range(N)]
list.sort(key=lambda x: x[1], reverse=True)
result = 0
for w, m in list:
    if W-w >= 0:
        result += (w*m)
        W -= w
    else:
        result += (W)*m
        break
print(result)
