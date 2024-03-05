class Solution:
    def minimumLength(self, s: str) -> int:
        l=[0]
        i=0
        c=0
        j=len(s)-1
        while i<j:
            if s[i]==s[j]:
                c+=2
                l[0]=s[i]
                i+=1
                j-=1
            elif s[i]!=s[j]:
                if s[i]==l[0]:
                    c+=1
                    i+=1
                elif s[j]==l[0]:
                    c+=1
                    j-=1
                else:
                    return len(s)-c
        if i==j:
            if s[i]==l[0]:
                c+=1
        

        return len(s)-c

         


                
    
            

        