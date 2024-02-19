class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        c=0
        d=0
        if n==0:
            return False
        else:

            for i in range(32): 
                if n & 1<< i > 0:
                    c=(2**i)
                if c==n:
                    d+=1
                    return True
            if d==0:
                return False


        