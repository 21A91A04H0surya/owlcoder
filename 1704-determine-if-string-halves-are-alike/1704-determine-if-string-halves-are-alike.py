class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        l=len(s)//2
        s1=s[:l]
        s2=s[l:]
        v="AEIOUaeiou"
        c1=0
        c2=0
        for i in range(len(s1)):
            if s1[i] in v:
                c1+=1
            if s2[i] in v:
                c2+=1
        if c1==c2:
            return True
        else:
            return False
        