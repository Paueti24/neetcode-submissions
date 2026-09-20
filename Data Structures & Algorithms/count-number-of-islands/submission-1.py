class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])
        visited = [[False] * n for _ in range(m)]
        count = 0

        def bfs(pos):
            queue = deque()
            queue.append(pos)
            visited[pos[0]][pos[1]] = True
            while queue:
                i, j = queue.popleft()

                neighbors = [(i+1,j), (i-1,j), (i,j+1), (i,j-1)]
                for ii, jj in neighbors:
                    if 0 <= ii and ii <= m - 1 and 0 <= jj and jj <= n - 1 and (not visited[ii][jj]) and grid[ii][jj] == '1':
                        queue.append((ii, jj))
                        visited[ii][jj] = True
        
        for i in range(m):
            for j in range(n):
                if not visited[i][j] and grid[i][j] == '1':
                    bfs((i,j))
                    count += 1
        
        return count


