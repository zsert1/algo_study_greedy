# 개미전사
# 최소 한칸 이상 떨어진 식량 창고 약탈
# a(i)=i번째 식량창고 까지의 최적의 해
# 특정한 i번째 식량창고에 대해서 털지 안털지 여부를 결정하여 더 많이 털 수 있는 경우를 선택
# 점화식으로 표현 ki= i벙째 식량창고에 있는 식량의 값
# a(i)=max(a(i-1),a(i-2)+k(i))
# 한칸 떨어져 있으므로 (i-3)은 번째 이하는 고려 필요(x)
n = int(input())
rice = list(map(int, input().split()))
d = [0]*100
d[0] = rice[0]
# 둘중 더큰 값을 알아야 한다.
d[1] = max(rice[0], rice[1])
for i in range(2, n):
    d[i] = max(d[i-1], d[i-2]+rice[i])
print(d[n-1])
