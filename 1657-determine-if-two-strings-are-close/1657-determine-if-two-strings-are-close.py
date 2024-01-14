from collections import Counter
class Solution:
    def closeStrings(self, w1: str, w2: str) -> bool:
        dic1=Counter(w1)
        dic2=Counter(w2)
        k1=[]
        k2=[]
        v1=[]
        v2=[]
        for k,v in dic1.items():
            k1.append(k)
            v1.append(v)
        k1.sort()
        v1.sort()
        for k,v in dic2.items():
            k2.append(k)
            v2.append(v)
        k2.sort()
        v2.sort()
        if k1==k2 and v1==v2:
            return True
        else:
            return False
            
        
        
        
        