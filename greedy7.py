# 나이트 문제
# 특정 위치에서 이동할 수 있는 경우의 수
# 행위치 1~n 열 위치 알파벳 순으로
# 완전 탐색
startPoint = input()
row = int(startPoint[1])
# 문자값을 아스키 코드 값으로 만들고 'a'의 아스키 코드값으로 빼고 +1을 해주어 스테이지의 위치를 적용한다
coloum = int(ord(startPoint[0]))-int(ord('a'))+1
# 나이트가 이동할 8가지 방향저장
steps = [(-2, -1), (-1, -2), (1, -2), (2, -1),
         (2, 1), (1, 2), (-1, 2), (-2, 1)]

result = 0
for step in steps:
    next_row = row+step[0]
    next_column = coloum+step[1]
    # 위치가 스테이지 위인지 파악
    if next_row >= 1 and next_row <= 8 and next_column >= 1 and next_column <= 8:
        result += 1

print(result)
