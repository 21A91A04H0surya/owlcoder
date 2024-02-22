from typing import List
class Solution:
    def dfs(self,adj,i,p,vis):
        vis[i]=1
        for j in adj[i]:
            
            if vis[j]==0:
                if(self.dfs(adj,j,i,vis)):return True
            elif(p != j):
                return True
        return False;
    #Function to detect cycle in an undirected graph.
	def isCycle(self, n: int, adj: List[List[int]]) -> bool:
		#Code here
		vis=[0 for i in range(n)]
		for i in range(n):
		    if vis[i]==0 and self.dfs(adj,i,-1,vis):return True
	    return False


#{ 
 # Driver Code Starts

if __name__ == '__main__':

	T=int(input())
	for i in range(T):
		V, E = map(int, input().split())
		adj = [[] for i in range(V)]
		for _ in range(E):
			u, v = map(int, input().split())
			adj[u].append(v)
			adj[v].append(u)
		obj = Solution()
		ans = obj.isCycle(V, adj)
		if(ans):
			print("1")
		else:
			print("0")

# } Driver Code Ends