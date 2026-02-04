# 점프왕쩰리
N = int(input())

MAP = []

for _ in range(N):
    MAP.append(list(map(int, input().split())))

visited = [[False] * N for _ in range(N)]
success = False

def dfs(x,y):
  global success

  if x < 0 or x >= N or y < 0 or y >= N:
        return

  if visited[x][y] == True:
    return

  
  visited[x][y] = True
  if MAP[x][y] == -1:
    success = True
    return

  jump = MAP[x][y]

  if jump==0:
    return

  dfs(x+MAP[x][y],y)
  dfs(x,y+MAP[x][y])


dfs(0,0)

if success:
    print("HaruHaru")
else:
    print("Hing")