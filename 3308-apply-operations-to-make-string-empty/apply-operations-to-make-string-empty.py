from collections import Counter
class Solution:
    def lastNonEmptyString(self, s: str) -> str:
        d={}
        for i in s:
            if i not in d:
                d[i]=1
            else:
                d[i]+=1
                
        print(d)
            
        maxi=0
        for v in d.values():
            if v > maxi:
                maxi=v
        for i in range(maxi-1):
            for k,v in d.items():
                d[k]=v-1
        st=""
        for i in range(len(s)-1,-1,-1):
            if s[i] in d and d[s[i]]>0:
                st=s[i]+st
                d[s[i]]-=1
        return st
            
    
            
            
        