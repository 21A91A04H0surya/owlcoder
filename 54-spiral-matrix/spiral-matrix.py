class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix:
            return 0
        l=[]
        left,top=0,0
        rows=len(matrix)
        cols=len(matrix[0])
        right=cols-1
        bottom=rows-1
        while left <= right and top <=bottom:
            for i in range(left,right+1):
                l.append(matrix[top][i])
            top+=1
            for i in range(top,bottom+1):
                l.append(matrix[i][right])
            right-=1
            if top <= bottom:
                for i in range(right,left-1,-1):
                    l.append(matrix[bottom][i])      
                bottom-=1
            if left <= right:
                for i in range(bottom,top-1,-1):
                    l.append(matrix[i][left])
                left+=1
        return l