#User function Template for python3


class Solution:
    def find(self, arr, n, x):
        
        # code here
        d={}
        for i in range(len(arr)):
            if arr[i] not in d:
                d[arr[i]]=[i]
            else:
                d[arr[i]]+=[i]
        for k,v in d.items():
            if k == x:
                if len(v)==1:
                    return v[0],v[0]
                else:
                    return v[0],v[-1]
        return -1,-1



#{ 
 # Driver Code Starts
t=int(input())
for _ in range(0,t):
    l=list(map(int,input().split()))
    n=l[0]
    x=l[1]
    arr=list(map(int,input().split()))
    ob = Solution()
    ans=ob.find(arr,n,x)
    print(*ans)
# } Driver Code Ends