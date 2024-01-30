import math
class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        su=1
        if num==1:
            return False
        for i in range(2,int(math.sqrt(num))+1):
            if num%i==0:
                if num//i==i:
                    su+=i
                else:
                    su+=i
                    su+=(num//i)

        if su==num:
            return True
        else:
            return False
                
        