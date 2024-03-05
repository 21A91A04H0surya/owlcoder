class Solution:
    def minimumLength(self, s: str) -> int:
        v=0
        i=0
        d=len(s)
        c=0
        j=len(s)-1
        while i<j:
            if s[i]==s[j]:
                c+=2
                v=s[i]
                i+=1
                j-=1
            elif s[i]!=s[j]:
                if s[i]==v:
                    c+=1
                    i+=1
                elif s[j]==v:
                    c+=1
                    j-=1
                else:
                    return d-c
        if i==j:
            if s[i]==v:
                c+=1
        

        return d-c

         


                
    
            

        