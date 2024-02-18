class Solution:
    def love(self,i,j,m,n,image,visited,color):
        if i <0 or j <0 or i >=m or j>=n or visited[i][j]==1 or image[i][j]!=d:
            return
        visited[i][j]=1
        image[i][j]=color
        self.love(i+1,j,m,n,image,visited,color)
        self.love(i,j+1,m,n,image,visited,color)
        self.love(i-1,j,m,n,image,visited,color)
        self.love(i,j-1,m,n,image,visited,color)
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        r=len(image)
        c=len(image[0])
        global d
        d=image[sr][sc]
        visited=[[0]*c for i in range(r)]
        self.love(sr,sc,r,c,image,visited,color)
        return image



        