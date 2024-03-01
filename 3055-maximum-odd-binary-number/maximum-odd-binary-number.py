from collections import Counter
class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        l=['0' for i in range(len(s))]
        d=Counter(s)
        v=d['1']
        l[-1]='1'
        v-=1
        f=''
        for i in range(len(l)):
            if v==0:
                break
            l[i]='1'
            v-=1
        print(l)
        return ''.join(l)

            
            




        
        
