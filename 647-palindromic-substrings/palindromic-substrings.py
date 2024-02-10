class Solution:
    def countSubstrings(self, s: str) -> int:
        l=list(s)
        ct=0
        for i in range(len(l)):
            for j in range(i,len(l)):
                d=l[i:j+1]
                c=d.copy()
                c.reverse()
                if c==d:
                    ct+=1

        return ct
        