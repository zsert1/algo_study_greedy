N, M, K = map(int, input().split())
graph = []
visite = [[False]*M for _ in range(N)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
for i in range(N):
    graph.append([0]*M)

for i in range(K):
    x, y = map(int, input().split())
    graph[x-1][y-1] = 1


def dfs(x, y):
    global cnt
    for i in range(4):
        nx = x+dx[i]
        ny = y+dy[i]
        if graph[nx][ny] == 1 and not visite[nx][ny]:
            visite[nx][ny] = True
            cnt += 1
            dfs(nx, ny)


result = 0
for i in range(N):
    for j in range(M):
        # 현재 위치에서 dfs수행
        if graph[i][j] == 1 and not visite[i][j]:
            cnt = 0
            dfs(i, j)
            result = max(result, cnt)
print(result)
