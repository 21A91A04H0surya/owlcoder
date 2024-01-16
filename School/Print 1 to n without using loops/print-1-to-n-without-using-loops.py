#User function Template for python3

class Solution:
    def printTillN(self, n):
    	#code here 
    	if n==0:
    	    return
    	self.printTillN(n-1)
    	print(n,end=" ")
    	


#{ 
 # Driver Code Starts
#Initial Template for Python 3


if __name__ == '__main__': 
    t = int(input())
    for _ in range(t):
        N = int(input())
        ob = Solution()
        ob.printTillN(N)
        print()
# } Driver Code Ends