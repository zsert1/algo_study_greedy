# 1로 만들기
# a(i)=i를 1로만들기 위한 최소 연산횟수
# 점화식 a(i)=min(a(i-1),a(i/2),a(i/3),a(i/5))+1
# 해당 수로 나누어 떨어질때 한해 점화식 사용가능
x = int(input())
d = [0]*30001


for i in range(2, x+1):
    d[i] = d[i-1]+1
    if i % 2 == 0:
        d[i] = min(d[i], d[i//2]+1)
    if i % 3 == 0:
        d[i] = min(d[i], d[i//3]+1)
    if i % 5 == 0:
        d[i] = min(d[i], d[i//5]+1)
print(d[x])
