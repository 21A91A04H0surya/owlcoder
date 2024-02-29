class Solution:
    def code(self,i,j,m,n,visited,grid,ct):
        if i < 0 or j <0 or i>m-1 or j > n-1 or grid[i][j]==0 or visited[i][j]==1:
            return
        visited[i][j]=1
        ct[0]+=1
        self.code(i+1,j,m,n,visited,grid,ct)
        self.code(i,j+1,m,n,visited,grid,ct)
        self.code(i-1,j,m,n,visited,grid,ct)
        self.code(i,j-1,m,n,visited,grid,ct)
        return ct

    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m=len(grid)
        maxi=0
        n=len(grid[0])
        visited=[[0]*n for i in range(m)]
        global result
        result=[]
        for i in range(m):
            for j in range(n):
                ct=[0]
                if grid[i][j]==1 and visited[i][j]==0:
                    d=(self.code(i,j,m,n,visited,grid,ct))
                    if d[0] > maxi:
                        maxi=d[0]
        return maxi
        
        