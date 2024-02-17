class Solution:
    def crush(self,i,j,grid,visited,m,n):
        if i >=0 and j>=0 and i<m and j < n and visited[i][j]=='0' and grid[i][j] == '1':
            visited[i][j]='1'
            self.crush(i+1,j,grid,visited,m,n)
            self.crush(i,j+1,grid,visited,m,n)
            self.crush(i,j-1,grid,visited,m,n)
            self.crush(i-1,j,grid,visited,m,n)



    def numIslands(self, grid: List[List[str]]) -> int:
        m=len(grid)
        n=len(grid[0])
        visited=[['0']*(n+1) for i in range(m)]
        c=0
        for i in range(m):
            for j in range(n):
                if grid[i][j]=='1' and visited[i][j]=='0':
                    c+=1
                    self.crush(i,j,grid,visited,m,n)
        return c
        