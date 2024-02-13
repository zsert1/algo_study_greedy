# 첫 째줄에는 끊어진 줄의 갯수 N개 와 파는 브랜드 걋수 K개
N, K = map(int, input().split())
package = []
single = []
minMoney = 0
# k개 만큼 돌면서 세트 6개 가격 낱개 가격 받는다.
for i in range(K):
    a, b = map(int, input().split())
    package.append[a]
    single.append[b]
min_package = min(package)
while N > 0:
    if N >= 6:
        min_single = min(single)*6
        N -= 6
    else:
        min_single = min(single)*N
        N -= N
    if min_single < min_package:
        minMoney += min_single
    else:
        minMoney += min_package
