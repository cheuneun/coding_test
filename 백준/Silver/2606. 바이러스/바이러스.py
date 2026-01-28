from collections import deque

n = int(input())
m = int(input())

graph = [ [] for i in range(n+1)]

for _ in range(m):
  a,b = map(int,input().split())
  graph[a].append(b)
  graph[b].append(a)

visited = [False] * (n+1)
result = []

def dfs(curr):
  visited[curr] = True
  result.append(curr)

  for next in graph[curr]:
    if not visited[next]:
      dfs(next)

dfs(1)
print(len(result)-1)