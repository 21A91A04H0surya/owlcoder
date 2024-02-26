
class Solution:
    def pat(self,s):
        res=[]
        dic={}
        k=0
        for i in s:
            if i in dic:
                res.append(dic[i])
            else:
                k+=1
                dic[i]=k
                res.append(k)
        return res
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        w=self.pat(pattern)
        out=[]
        for i in words:
            if self.pat(i)==w:
                out.append(i)
        return out

        
        