class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        d=[]
        l=[]
        n=len(matrix[0])
        o=[0 for _ in range(n)]
        for i in matrix:
            for j in range(len(i)):
                if i[j]==0:
                    d.append(j)
                    l.append(i)
        for i in matrix:
            if i in l:
                i[::]=o[::]    
        for i in d:
            for j in matrix:
                j[i]=0
        return matrix

       
                




        