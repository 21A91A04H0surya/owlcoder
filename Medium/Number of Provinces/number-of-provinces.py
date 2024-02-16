#User function Template for python3

class Solution:
    def fun(self,no,l,visited):
        if visited[no]==0:
            visited[no]=1
            t=l[no]
            for i in t:
                self.fun(i,l,visited)
            
            
    def numProvinces(self, adj, v):
        # code here 
        l=[]
        l.append([])
        for i in adj:
            o=[]
            for j in range(len(i)):
                if i[j] == 1:
                    o.append(j+1)
            l.append(o)
        visited=[0 for i in range(v+1)]
        c=0
        for i in range(1,v+1):
            if visited[i]==0:
                c+=1
                self.fun(i,l,visited)
        return c
            
                
        
        



#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        V=int(input())
        adj=[]
        
        for i in range(V):
            temp = list(map(int,input().split()))
            adj.append(temp);
        
        ob = Solution()
        print(ob.numProvinces(adj,V))
# } Driver Code Ends