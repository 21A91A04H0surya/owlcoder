class Solution:
    def fun(self,i,j,m,n,image,visited,nc,d):
        if i <0 or j < 0 or i >=m or j >=n or visited[i][j]==1:
            return
        visited[i][j]=1
        if image[i][j]==d:
            image[i][j]=nc
            self.fun(i+1,j,m,n,image,visited,nc,d)
            self.fun(i-1,j,m,n,image,visited,nc,d)
            self.fun(i,j+1,m,n,image,visited,nc,d)
            self.fun(i,j-1,m,n,image,visited,nc,d)
        
        
        
	def floodFill(self, image, sr, sc, nc):
		#Code here
		m=len(image)
		n=len(image[0])
		d=image[sr][sc]
		visited=[[0]*(n) for i in range(m)]
	    self.fun(sr,sc,m,n,image,visited,nc,d)
	    return image
		



#{ 
 # Driver Code Starts
import sys
sys.setrecursionlimit(10**7)


T=int(input())
for i in range(T):
	n, m = input().split()
	n = int(n)
	m = int(m)
	image = []
	for _ in range(n):
		image.append(list(map(int, input().split())))
	sr, sc, newColor = input().split()
	sr = int(sr); sc = int(sc); newColor = int(newColor);
	obj = Solution()
	ans = obj.floodFill(image, sr, sc, newColor)
	for _ in ans:
		for __ in _:
			print(__, end = " ")
		print()
# } Driver Code Ends