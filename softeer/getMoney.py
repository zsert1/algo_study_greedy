# 금고털이
w, n = map(int, input().split())


result = 0
weigths = [list(map(int, input().split())) for _ in range(n)]
weigths.sort(key=lambda x: x[1], reverse=True)
for weigth, money in weigths:
    if w-weigth >= 0:
        result += (money*weigth)
        w -= weigth
    else:
        result += (w*money)
        break


print(result)
