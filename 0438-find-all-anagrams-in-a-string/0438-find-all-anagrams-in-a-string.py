class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        d=''.join(sorted(list(p)))
        l=len(p)
        o=[]
        for i in range(len(s)-l+1):
            w=s[i:l]
            
            d1=''.join(sorted(w))
            if d1==d:
                o.append(i)
            i+=1
            l+=1
        return o
