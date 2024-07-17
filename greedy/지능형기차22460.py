def max_passengers():
    current_passengers = 0
    max_passengers = 0

    for _ in range(10):
        out, in_ = map(int, input().split())
        current_passengers -= out  # 내린 사람 수 빼기
        current_passengers += in_  # 탄 사람 수 더하기
        if current_passengers > max_passengers:
            max_passengers = current_passengers  # 최대 승객 수 갱신

    print(max_passengers)


max_passengers()
