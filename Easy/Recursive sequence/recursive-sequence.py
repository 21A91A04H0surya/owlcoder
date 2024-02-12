#User function Template for python3

class Solution:
    def sequence(self, n):
        k=1
        t=0
        mod=int(1e9+7)
        for i in range(1,n+1):
            s=1
            for j in range(i):
                s=(s%mod)*(k%mod)
                k+=1
            t+=s
        return t%mod
           
            


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())
        
        ob = Solution()
        print(ob.sequence(N))
# } Driver Code Ends