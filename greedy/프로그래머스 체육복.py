def solution(n, lost, reserve):
    answer = 0
    # set를 이용하여 고유한 애들만 남김
    reamin_reserve = set(reserve)-set(lost)
    reamin_lost = set(lost)-set(reserve)
    # 양옆에 확인
    for i in reamin_reserve:
        if i-1 in reamin_lost:
            reamin_lost.remove(i-1)
        elif i+i in reamin_lost:
            reamin_lost.remove(i+1)
    answer = n-len(reamin_lost)
    return answer
