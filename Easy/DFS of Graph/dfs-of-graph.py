#User function Template for python3

class Solution:
    
    #Function to return a list containing the DFS traversal of the graph.
    def fun(self,id,adj,res,visited):
        if visited[id]==0: 
            res.append(id)
            visited[id]=1
            t=adj[id]
            for i in t:
                if visited[i] ==0:
                   self.fun(i,adj,res,visited)
        return res
        
    def dfsOfGraph(self, node, adj):
        # code here
        res=[]
        visited=[0 for i in range(node+1)]
        return self.fun(0,adj,res,visited)


#{ 
 # Driver Code Starts

if __name__ == '__main__':
    T=int(input())
    while T>0:
        V,E=map(int,input().split())
        adj=[[] for i in range(V+1)]
        for i in range(E):
            u,v=map(int,input().split())
            adj[u].append(v)
            adj[v].append(u)
        ob=Solution()
        ans=ob.dfsOfGraph(V,adj)
        for i in range(len(ans)):
            print(ans[i],end=" ")
        print()
        T-=1
# } Driver Code Ends