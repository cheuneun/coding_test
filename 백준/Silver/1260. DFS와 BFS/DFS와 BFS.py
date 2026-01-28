# 최종코드
from collections import deque

N, M, V = map(int, input().split())

graph = [[] for _ in range(N+1)]

for _ in range(M): # 인접리스트 생성
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(1,N+1):
  graph[i].sort()

dfs_visited = [False] * (N+1)
dfs_result = []

def dfs(curr):
  dfs_visited[curr] = True
  dfs_result.append(curr)

  for next in graph[curr]:
      if not dfs_visited[next]:
          dfs(next)

dfs(V)
print(*dfs_result)


bfs_visited = [False] * (N+1)
bfs_result = []

def bfs(V):
  queue = deque()
  queue.append(V)
  bfs_visited[V] = True

  while queue:
      curr = queue.popleft()
      bfs_result.append(curr)
      for next in graph[curr]:
          if not bfs_visited[next]:
              queue.append(next)
              bfs_visited[next] = True

bfs(V)
print(*bfs_result)