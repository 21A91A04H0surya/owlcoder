class Solution:
    def mia(self,i,j,m,n,l):
        if i>=m or j >= n or l[i][j]==1:
            return 0
        if i == m-1 and j == n-1:
            return 1
        
        # if l[i][j]==1:
        #     return 0
        if dp[i][j]!=-1:
            return dp[i][j]
        dp[i][j]=self.mia(i+1,j,m,n,l)+self.mia(i,j+1,m,n,l)
        return dp[i][j]
    def uniquePathsWithObstacles(self, l: List[List[int]]) -> int:
        m=len(l)
        n=len(l[0])
        global dp
        dp=[[-1]*101 for i in range(101)]
        return self.mia(0,0,m,n,l)
    
        