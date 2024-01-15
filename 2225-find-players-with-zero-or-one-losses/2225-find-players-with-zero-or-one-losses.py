from collections import Counter
class Solution:
    def findWinners(self, m: List[List[int]]) -> List[List[int]]:
        l1=[]
        l2=[]
        for i in m:
            l1.append(i[0])
            l2.append(i[1])
        p1=[]
        p2=[]
        o=[]
        dic1=Counter(l1)
        dic2=Counter(l2)
        for i in dic1:
            if i not in dic2:
                p1.append(i)
        for k,v in dic2.items():
            if v==1:
                p2.append(k)
        p1.sort()
        p2.sort()
        o.append(p1)
        o.append(p2)
        return o
        
        