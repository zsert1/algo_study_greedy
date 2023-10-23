# 최대 공약수 계산(유클리드 호제법)
def gcd(a, b):
    if a % b == 0:
        return b
    else:
        # 0이 아닌 경우 나머지를 두번째 인자를 넣어준다
        return gcd(b, a % b)


print(gcd(192, 162))
