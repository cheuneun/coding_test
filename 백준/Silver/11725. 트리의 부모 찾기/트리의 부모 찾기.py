import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

N = int(input())

graph = [ [] for _ in range(N+1)]
for _ in range(N-1): # 간선의 수,,,
  a,b = map(int, input().split())
  graph[a].append(b)
  graph[b].append(a)

parent = [0] * (N+1)
parent[1] = 1

def dfs(curr):
  for next in graph[curr]:
      if parent[next] == 0:
        parent[next] = curr
        dfs(next)


dfs(1)
for i in range(2,N+1):
  print(parent[i])