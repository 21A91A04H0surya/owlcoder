class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        c=0
        if n==1:
            return True
        else:
            i=1
            while 3**i<=n:
                if 3**i ==n:
                    c+=1
                    return True
                i+=1
            if c==0:
                return False
                
                
            
        
        