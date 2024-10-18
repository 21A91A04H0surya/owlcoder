class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        rows=len(mat)
        cols=len(mat[0])
        top,left=0,0
        right=cols-1
        bottom=rows-1
        val=0
        val=top+bottom
        if val%2==0:
            idx=val//2       
            ds=0
            for i in range(bottom+1):
                ds+=mat[i][i]
            le=left
            for i in range(right,left-1,-1):
                ds+=mat[le][i]
                le+=1
            return ds-mat[idx][idx]
        else:
            ds=0
            for i in range(bottom+1):
                ds+=mat[i][i]
            le=left
            for i in range(right,left-1,-1):
                print(mat[le][i])
                ds+=mat[le][i]
                le+=1
            return ds

        