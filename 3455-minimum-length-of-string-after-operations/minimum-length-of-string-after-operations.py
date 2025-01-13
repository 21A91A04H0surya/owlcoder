from collections import Counter
class Solution:
    def minimumLength(self, s: str) -> int:
        reslen=0
        dic=Counter(s)
        for v in dic.values():
            if v%2==0:
                reslen+=2
            else:
                reslen+=1
        return reslen
        
        