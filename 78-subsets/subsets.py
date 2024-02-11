class Solution:
    def xxx(self,ind,l,res,temp,n):
        if ind==n:
            c=temp.copy()
            res.append(c)
            return 
        self.xxx(ind+1,l,res,temp+[l[ind]],n)
        self.xxx(ind+1,l,res,temp,n)
        return res
        
        

    def subsets(self, l: List[int]) -> List[List[int]]:
        res=[]
        temp=[]
        n=len(l)
        return self.xxx(0,l,res,temp,n)
                
            
        
        