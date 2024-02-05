class Solution:
    def combi(self,ind,n,k,result,temp):
        if len(temp)==k:
            c=temp.copy()
            result.append(c)
            return
        for i in range(ind,n+1):
            temp.append(i)
            self.combi(i+1,n,k,result,temp)
            temp.pop()


    def combine(self, n: int, k: int) -> List[List[int]]:
        result=[]
        temp=[]
        self.combi(1,n,k,result,temp)
        return result
        