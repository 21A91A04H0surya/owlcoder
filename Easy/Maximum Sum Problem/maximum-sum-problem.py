#User function Template for python3

class Solution:
    global dp
    dp=[-1 for i in range(1000000)]
    def maxSum(self, n): 
        # code here 
        if n==0:
            return 0
        if dp[n]!=-1:
            return dp[n]
        a=self.maxSum(n//2)
        b=self.maxSum(n//3)
        c=self.maxSum(n//4)
        dp[n]= max((a+b+c),n)
        return dp[n]
        



#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int(input())
    for _ in range(t):
        n = int(input())
        ob = Solution()
        print(ob.maxSum(n))
# } Driver Code Ends