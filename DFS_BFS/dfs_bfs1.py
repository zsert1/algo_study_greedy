# 음료수 얼려먹기
# 상하 좌우 로 연결되오 있다고 표현 가능
# 인접한 노드 형태로 표현가능
# 특정 지점에 연결된 모든 노드를 방문 처리
# 1. 특정 지점 상,하,좌,우 주변 지점 중에서 값이 0 이면서 아직 방문하지 않은 지점이 있다면 방문처리
# 2. 방문 지점 상하좌우 살피고 방문 진해과정 반복 하면 연결된 모든 노드 방문
# 3.모든 노드에 대하여 1~2번 과정 방문, 방문하지 않은 지점 수 카운트
# 0이 뚫린것 1이 막힌것
# 연결 노드의 갯수
n, m = map(int, input().split())
graph = []
# 2차원 리스트에 맵정보 입력 받기
for _ in range(n):
    graph.append(list(map(int, input())))


def dfs(x, y):
    # 주어진 범위 벗어나면 즉시 종료
    if x <= -1 or x >= n or y <= -1 or y >= m:
        return False
    # 현재 노드 아직 방문하지 않았다면
    if graph[x][y] == 0:
        # 방문처리
        graph[x][y] = 1
        # 상하좌우 위치들도 모두 재귀적으로 호출
        dfs(x-1, y)
        dfs(x, y-1)
        dfs(x+1, y)
        dfs(x, y+1)
        return True
    return False


result = 0
for i in range(n):
    for j in range(m):
        # 현재 위치에서 dfs수행
        if dfs(i, j) == True:
            result += 1
print(result)
