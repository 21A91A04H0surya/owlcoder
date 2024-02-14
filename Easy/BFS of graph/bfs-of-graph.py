#User function Template for python3

from typing import List
from queue import Queue
class Solution:
    #Function to return Breadth First Traversal of given graph.
    def fuckthelife(self,nude,visitedgoa,condom,hot):
        porn=[]
        porn.append(nude)
        visitedgoa[nude]=1
        while len(porn)!=0:
            pennis=porn[0]
            condom.append(pennis)
            porn.pop(0)
            for sex in hot[pennis]:
                if visitedgoa[sex]!=1:
                    porn.append(sex)
                    visitedgoa[sex]=1
        return condom
    def bfsOfGraph(self, node: int, hot: List[List[int]]) -> List[int]:
        # code here
        edge=node-1
        condom=[]
        visitedgoa=[0 for i in range(node+1)]
        return self.fuckthelife(0,visitedgoa,condom,hot)
        


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
		ob = Solution()
		ans = ob.bfsOfGraph(V, adj)
		for i in range(len(ans)):
		    print(ans[i], end = " ")
		print()
        

# } Driver Code Ends