class Solution:
    def makeSmallestPalindrome(self, s: str) -> str:
        l=list(s)
        i=0
        j=len(s)-1
        while i <= j:
            if l[i] > l[j]:
                l[i]=l[j]
            else:
                l[j]=l[i]  
            i+=1
            j-=1
        return ''.join(l)

            
        


        