class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        tc=[0]*(n+1)
        for p1,p2 in trust:
            tc[p1]-=1
            tc[p2]+=1
        for i in range(1,n+1):
            if tc[i]==n-1:
                return i
        return -1
        

        
        


        

    
        

        