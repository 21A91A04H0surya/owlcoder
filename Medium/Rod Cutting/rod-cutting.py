#User function Template for python3
import sys
sys.setrecursionlimit(100000000)

class Solution:
    def fun(self,prices,le,dp):
        sumi = 0
        if le == 0: 
            return 0
        if dp[le]!=-1:
            return dp[le]
        for i in range(0,le):
            sumi=max(sumi,prices[i]+self.fun(prices,le-(i+1),dp))
        dp[le]=sumi
        return dp[le]
    def cutRod(self, prices, le):
        #code here
        dp=[-1]*(le+1)
        return (self.fun(prices,le,dp))


#{ 
 # Driver Code Starts
#Initial Template for Python 3

def main():

    T = int(input())

    while(T > 0):
        n = int(input())
        a = [int(x) for x in input().strip().split()]
        ob = Solution()
        print(ob.cutRod(a, n))

        T -= 1


if __name__ == "__main__":
    main()
# } Driver Code Ends