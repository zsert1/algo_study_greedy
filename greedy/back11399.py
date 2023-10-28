
# ATM
N = int(input())
times = list(map(int, input().split()))
times.sort()
result = 0
for x in range(1, N+1):
    # 슬라이싱을 통한 특정 인뎃스 까지 합 계속 더해준다
    result += sum(times[0:x])
print(result)
