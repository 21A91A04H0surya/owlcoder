from collections import Counter
class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        l=[]
        o=[]
        maxi=0
        f=0
        for i in edges:
            l+=i
        d=Counter(l)
        for k,v in d.items():
            if v > maxi:
                maxi = v
                f=k
        return f
        

        