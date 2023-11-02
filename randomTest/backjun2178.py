from collections import deque

N, M = map(int, input().split())
graph = []
for i in range(N):
    graph.append(list(map(int, input())))
check = [[0]*M for _ in range(N)]
dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]
q = deque()
q.append([0, 0])
check[0][0] = 1
while q:
    x, y = q.popleft()
    for i in range(4):
        nx, ny = x+dx[i], y+dy[i]
        if 0 <= nx < N and 0 <= ny < M and check[nx][ny] == 0 and graph[nx][ny] == 1:
            q.append([nx, ny])
            check[nx][ny] = check[x][y]+1

print(check[-1][-1])
