#User function Template for python3

import sys
sys.setrecursionlimit(10**8)

    
class Solution:
    def fun(self,i,j,grid,visited,m,n):
        visited[i][j]=1
        for x in range(-1,2,1):
            for y in range(-1,2,1):
                nrow = i + x;
                ncol = j + y;
                if(nrow >=0 and nrow < m and ncol >= 0 and ncol < n and grid[nrow][ncol]==1 and visited[nrow][ncol] ==0):
                    self.fun(nrow,ncol,grid,visited,m,n)
    def numIslands(self,grid):
        #code here
        m=len(grid)
        n=len(grid[0])
        visited=[[0]*(n)  for i in range(m)]
        c=0
        for i in range(m):
            for j in range(n):
                if grid[i][j]==1 and visited[i][j] == 0:
                    c+=1
                    self.fun(i,j,grid,visited,m,n)
        return c
                    
                
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__=="__main__":
    for _ in range(int(input())):
        n,m=map(int,input().strip().split())
        grid=[]
        for i in range(n):
            grid.append([int(i) for i in input().strip().split()])
        obj=Solution()
        print(obj.numIslands(grid))
# } Driver Code Ends