X, Y, W, S = map(int, input().split())
time = 0

if 2*W <= S:
    print((X+Y)*W)
else:
    small = min(X, Y)
    time = small*S
    absXY = abs(X-Y)
    if W > S:
        # 짝수인 경우
        if absXY % 2 == 0:
            time += absXY*S
        else:
            # 짝수로 만든다
            time += (absXY-1)*S+W
    else:
        # 2*W가 작은 경우 기존 타임에 absXY*W를 더한다(대각선으로 간후 남은 단일 거리)
        time += absXY*W
    print(time)
