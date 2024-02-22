class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        l=[]
        for i in range(len(matrix)):
            o=[]
            for j in range(len(matrix)):
                o.append(matrix[j][i])
            o.reverse()
            l.append(o)
            
        matrix[::]=l
        