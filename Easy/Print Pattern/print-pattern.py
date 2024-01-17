#User function Template for python3
import sys
sys.setrecursionlimit(100000)
class Solution:
    def __init__(self):
        self.l=[]
    def pattern(self, n):
        if n <= 0:
            self.l.append(n)
            return self.l
        self.l.append(n)
        self.pattern(n-5)
        self.l.append(n)
        return self.l
        
        # code here
       
        
        
        
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())
        
        ob = Solution()
        ans = ob.pattern(N)
        for i in ans:
            print(i, end = " ")
        print()
# } Driver Code Ends