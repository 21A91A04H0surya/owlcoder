from collections import Counter
class Solution:
    def frequencySort(self, s: str) -> str:
        s=list(s)
        dic=Counter(s)
        l=list(zip(dic.values(),dic.keys()))
        l=sorted(l,reverse = True)
        stri=""
        for i in l:
            stri+=i[1]*i[0]
        return stri
   
            
            
                

        