# 상하좌우 문제
dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]
move_type = ['L', 'R', 'U', 'D']
startPointX, startPointY = 1, 1
n = int(input())
k = list(input().split())
for plan in k:
    for i in len(range(move_type)):
        if plan == move_type[i]:
            nx = startPointX + dx[i]
            ny = startPointY + dy[i]
    if nx < 1 or ny < 1 or nx > n or ny > n:
        continue
    x, y = nx, ny

print(x, y)
