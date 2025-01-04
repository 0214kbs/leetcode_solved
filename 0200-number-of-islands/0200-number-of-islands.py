from collections import deque
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        drc = [(-1,0),(1,0),(0,1),(0,-1)]
        n = len(grid)
        m = len(grid[0])

        def bfs(val, r,c):
            q = deque()
            q.append((r,c))
            while q:
                cr,cc = q.popleft()
                for dr, dc in drc:
                    nr, nc = cr+dr, cc+dc
                    if 0<=nr<n and 0<=nc<m and int(grid[nr][nc])>0:
                        grid[nr][nc] = str(val)
                        q.append((nr,nc))
            return
            
        cnt = 1
        for r in range(n):
            for c in range(m):
                if int(grid[r][c]) > 0:
                    grid[r][c] = str(-cnt)
                    bfs(-cnt, r,c)
                cnt += 1
        
        return cnt-1