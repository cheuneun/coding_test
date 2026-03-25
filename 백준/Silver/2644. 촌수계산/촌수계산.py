# 2644

n = int(input())
a,b = map(int, input().split())
m = int(input())
graph = [ [] for _ in range(n+1)]
for _ in range(m):
  x,y = map(int, input().split())
  graph[x].append(y)
  graph[y].append(x)

dist = [-1] * (n+1)

def dfs(curr,d):
  dist[curr] = d
  for next in graph[curr]:
      if dist[next] == -1:
        dfs(next, d + 1)

dfs(a,0)

print(dist[b])