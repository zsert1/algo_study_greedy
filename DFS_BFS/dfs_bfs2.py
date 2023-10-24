# 미로 탈출
# 0 괴물 존재
# bfs는 간선의 비용이 모두 같을 때 최단 거리 구할때 사용
# 상하좌우 연결된 모든 노드로의 거리가 1로 동일
# (1,1)지점 부터 BFS를 수행하여 모든 노드의 최단 거리값 기록하면 된다.
# 새롭게 방문하는 노드의 값을 2로 바꾼다.
# 매번 새로운 지점을 방문할 때 직전 노드의 거리에 +1을 한다.
from collections import deque
n, m = map(int, input().split())
graph = []
for i in range(n):
    graph.append(list(map(int, input())))
# 상하 좌우 4가지 방향 설정
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
result = 1


def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    # 큐가 빌때 까지 반복
    while queue:
        x, y = queue.popleft()
        # 현재 위치에서 4가지 방향으로 위치 확인
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                # 벽인 공간 무시
                if graph[nx][ny] == 0:
                    continue
                # 해당 노드 첫 방문인 경우에만 최단 거리 기록
                if graph[nx][ny] == 1:
                    graph[nx][ny] = graph[x][y]+1
                    queue.append((nx, ny))
        # 가장 오르쪽 아래까지 최단 거리 반환
        return graph[n-1][m-1]


print(bfs(0, 0))
