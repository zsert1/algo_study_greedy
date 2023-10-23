def dfs(graph, v, visited):
    # 현재 노드 방문 처리
    visited[v] = True
    for i in graph[v]:
        # 현재 노드와 연결된 다른 노드들 재귀적으로 방문 처리
        if not visited[i]:
            dfs(graph, i, visited)


# 인접 노드 구성 2중 배열로
graph = [[], [2, 3, 8], [1, 7], [1, 4, 5],
         [3, 5], [3, 4], [7], [2, 6, 8], [1, 7]]
# 인접 노드 방문 배열 수 만큼 false배열
visited = [False]*9
dfs(graph, 1, visited)
