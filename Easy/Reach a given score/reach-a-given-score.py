#User function Template for python3

class Solution:
    def count(self, n: int) -> int:
        #your code here
        v=[0 for i in range(n+1)]
        v[0]=1
        for i in range(3,n+1):
            v[i]+=v[i-3]
        for i in range(5,n+1):
            v[i]+=v[i-5]
        for i in range(10,n+1):
            v[i]+=v[i-10]
        return v[n]


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == "__main__":
    for _ in range(int(input())):
        n = int(input())
        ob = Solution()
        print(ob.count(n))
        
# } Driver Code Ends