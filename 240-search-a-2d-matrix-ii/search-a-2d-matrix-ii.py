class Solution:
    def dfs(self,i,j,m,n,matrix,target,vis):
        if i >= m-1 or j >= n-1 or vis[i][j]==1:
            return
        vis[i][j]=1
        if matrix[i][j]==target:
            return True
        self.dfs(i,j+1,m,n,matrix,target,vis)
        self.dfs(i+1,j,m,n,matrix,target,vis)



    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m=len(matrix)
        n=len(matrix[0])
        vis=[[0]*n for i in range(m)]
        for i in range(m):
            for j in range(n):
                if matrix[i][j]==target:
                    return True
                elif vis[i][j]==0 and matrix[i][j]!=target:
                    if self.dfs(i,j,m,n,matrix,target,vis):
                        return True
        return False
        