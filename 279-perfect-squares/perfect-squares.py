import math
class Solution:
    def fun(self,n,dp):
        #Base case
        if n ==0:
            return 0
        d=100001
        if dp[n] != -1:
            return dp[n]
        for i in range(1,int(math.sqrt(n))+1,1):
            if i*i <= n:
                d=min(d,1+self.fun(n-i*i,dp))  
        dp[n]=d
        return dp[n]        
    def numSquares(self, n: int) -> int:
        dp=[-1 for i in range(n+1)]
        t=0
        return(self.fun(n,dp))
        