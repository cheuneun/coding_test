from collections import deque

def solution(maps):
    answer = 0
    n, m = len(maps), len(maps[0])
    
    # 먼저 위치 찾기
    for i,val in enumerate(maps):
        for j,vval in enumerate(val):
            if vval=='S':
                start = (i,j)
            elif vval=='L':
                lever = (i,j)
            elif vval=='E':
                end=(i,j)
    
    
    def bfs(start,end):
        dx = [-1,1,0,0]
        dy = [0,0,-1,1]
    
        visited = [[-1]*m for _ in range(n)]
        
        queue = deque([start])
        visited[start[0]][start[1]] = 0
        
        while queue:
            x,y= queue.popleft()
            
            if (x,y) == end:
                return visited[x][y]
            
            # 4방향 탐색
            for i in range(4):
                nx, ny = x + dx[i], y + dy[i]
                
                if 0 <=nx< n and 0 <=ny<m:
                    if maps[nx][ny] != 'X' and visited[nx][ny] == -1:
                        visited[nx][ny] = visited[x][y] + 1
                        queue.append((nx,ny))
        return -1
                
    path1 = bfs(start, lever)
    path2 = bfs(lever, end)
            
    if path1 == -1 or path2 == -1:
        return -1
    return path1 + path2