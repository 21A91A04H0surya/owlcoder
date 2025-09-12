class Solution:
    def doesAliceWin(self, s: str) -> bool:
        str="aeiou"
        vc=0
        for i in s:
            if i in str:
                vc+=1
        if vc==0:
            return False
        return True


        