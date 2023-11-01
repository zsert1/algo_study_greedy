# bfs dfs 기본
from collections import deque
N, M, V = map(int, input().split())
graph = [[0]*(N+1) for _ in range(N+1)]
for i in range(M):
    a, b = map(input().split())
    # 연뎔된 노드는 1로 초기화
    graph[a][b] = graph[b][a] = 1

visited = [0]*(N+1)
visited2 = visited.copy()


def dfs(x):
    visited[x] = 1
    print(x, end='')
    for i in range(1, N+1):
        # 연결된 노드중에 방문한 기록이 없는 노드인 경우 재 호출
        if graph[x][i] == 1 and visited[i] == 0:
            dfs(i)


def bfs(V):
    queuq = deque([V])
    # 노드 방문처리
    visited2[V] = 1
    while queuq:

        V = queuq.popleft(0)
        print(V, end="")
        for i in range(1, N-1):
            #  방문한적 없고 노드가 연결되어 있다면
            if visited2[i] == 0 and graph[V][i] == 1:
                # 큐에 값을 넣어준다
                queuq.append(i)
                visited2[i] = 1
