#User function Template for python3

class Solution:
    def ratpath(self,i,j,m,extra,s,ans,n):
        if i==n-1 and j==n-1 :
            if m[i][j]==1:
                ans.append(s)
            return
        if i>=n or j>=n or i<0 or j <0:
            return
        if extra[i][j]==0:
            return
        if m[i][j]==0:
            return
        extra[i][j]=0
        down=self.ratpath(i+1,j,m,extra,s+'D',ans,n)
        left=self.ratpath(i,j-1,m,extra,s+'L',ans,n)
        right=self.ratpath(i,j+1,m,extra,s+'R',ans,n)
        up=self.ratpath(i-1,j,m,extra,s+'U',ans,n)
        extra[i][j]=1
        
            
        
        
    def findPath(self, m, n):
        # code here
        extra=[[1] * n for _ in range(n)]
        i=0
        j=0
        ans=[]
        self.ratpath(i,j,m,extra,"",ans,n)
        return ans
        
        
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__=='__main__':
    t = int(input())
    for i in range(t):
        n = list(map(int, input().strip().split()))
        arr = list(map(int, input().strip().split()))
        
        matrix = [[0 for i in range(n[0])]for j in range(n[0])]
        k=0
        for i in range(n[0]):
            for j in range(n[0]):
                matrix[i][j] = arr[k]
                k+=1
        ob = Solution()
        result = ob.findPath(matrix, n[0])
        result.sort()
        if len(result) == 0 :
            print(-1)
        else:
            for x in result:
                print(x,end = " ")
            print()
# } Driver Code Ends