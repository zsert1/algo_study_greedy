n = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
result = 0
for i in range(n):
    result += min(A)*max(B)
    # 최소값 제와
    A.pop(A.index(min(A)))
    # 최댓값 제외
    B.pop(B.index(max(B)))

print(result)
