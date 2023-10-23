from collections import deque


def bfs(graph, start, visited):
    queue = deque([start])
    # 현재 방문한 큐 방문처리
    visited[start] = True
    while queue:
        # 큐에서 하나으 원소 뽕아 출력
        v = queue.popleft()
        print(v, end='')
        # 아직 방문하지 않은 인접한 원소들을 큐에 삽입
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True


graph = [[], [2, 3, 8], [1, 7], [1, 4, 5],
         [3, 5], [3, 4], [7], [2, 6, 8], [1, 7]]
# 인접 노드 방문 배열 수 만큼 false배열
visited = [False]*9
bfs(graph, 1, visited)
