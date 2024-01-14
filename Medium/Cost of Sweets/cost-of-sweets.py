#User function Template for python3
class Solution:
    def costOfSweets (self, n):
        # code here 
        res=0
        for i in range(2,n+1,4):
            res+=-1
        ans=n+res
        return ans+res
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3
if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        M = int(input())
        
        ob = Solution()
        print(ob.costOfSweets(M))
# } Driver Code Ends