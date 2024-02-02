#User function Template for python3

class Solution:
    def perm(self,arr,n,temp,ans,visited,s,dic):
        if len(temp)==n:
            c=temp.copy()
            if s not in dic:
                dic[s]=1
                ans.append(c)
            return
        for i in range(len(arr)):
            if visited[i]==0:
                visited[i]=1
                temp.append(arr[i])
                self.perm(arr,n,temp,ans,visited,s+str(arr[i]),dic)
                temp.pop()
                visited[i]=0
    def uniquePerms(self, arr, n):
        # code here 
        arr.sort()
        temp=[]
        dic={}
        visited=[0]*n
        ans=[]
        self.perm(arr,n,temp,ans,visited,"",dic)
        return ans


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        n=int(input())
        arr=list(map(int,input().split()))
        
        ob = Solution()
        res = ob.uniquePerms(arr,n)
        for i in range(len(res)):
            for j in range(n):
                print(res[i][j],end=" ")
            print()
# } Driver Code Ends