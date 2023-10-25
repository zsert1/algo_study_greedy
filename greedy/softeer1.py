w, n = map(int, input().split())
result = 0
# list n의 갯수 만큼만들어준다
weigths = [list(map(int, input().split())) for _ in range(n)]
# lambda를 이용한 내림차순 정렬
weigths.sort(key=lambda x: x[1], reverse=True)
for weigth, money in weigths:
    if w-weigth >= 0:
        result += (money*weigth)
        w -= weigth
    else:
        result += (w*money)
        break


print(result)
