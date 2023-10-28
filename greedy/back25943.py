# # 저울 문제
# n = int(input())
# weights = list(map(int, input().split()))
# left = []
# right = []
# array = [1, 2, 5, 10, 20, 50, 100]
# array.sort(reverse=True)
# count = 0
# for i in range(0, n, 2):
#     left.append(weights[i])
#     if i >= 2 and i-1 < n:
#         right.append(weights[i-1])
# sumA = sum(left)
# sumB = sum(right)
# minus = sumA-sumB
# if minus == 0:
#     print(0)
# elif minus < 0:
#     minus*-1
# for ar in array:
#     count += minus//ar
#     minus %= ar

# print(count)
#  잘 못 짠 코드
# 아래가 맞게 짠코드
# 나와의 차이점은 왼쪽 오른쪽을 문제를 잘 못 해석하여 i,i+1인 것으로 구분하였는데
# 그것이 아닌 상황에 맞게 왼쪽에 자갈을 할지 오른쪽에 자갈을 올릴지 결정해야 한다.
n = int(input())
Pebbles = list(map(int, input().split()))  # 자갈들 무게
s = [0, 0]  # 저울의 왼쪽, 오른쪽

for p in Pebbles:
    if s[0] <= s[1]:  # 오른쪽이 무겁거나 같으면
        s[0] += p  # 왼쪽에 자갈 달기
    else:  # 왼쪽이 무거우면
        s[1] += p  # 오른쪽에 자갈 달기

diff = abs(s[0]-s[1])  # 남은 무게 차이
ans = 0  # 추가로 필요한 추의 개수

while diff:
    for w in (100, 50, 20, 10, 5, 2, 1):  # 무거운 추부터 꺼냄
        ans += diff//w  # w가 몇 개 필요한지 ans에 더하기
        diff %= w  # 무게가 w들을 추가로 달고 남은 무게

print(ans)
