class Solution:
    def subsets(self, l: List[int]) -> List[List[int]]:
        res=[]
        n=len(l)
        for i in range(2**n):
            o=[]
            for j in range(len(l)):
                if  i >> j & 1 > 0:
                    o.append(l[j])
            res.append(o)
        return res
                
            
        
        