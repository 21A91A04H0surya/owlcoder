from collections import Counter
class Solution:
    def getCommon(self, l1: List[int], l2: List[int]) -> int:
        dic1=Counter(l1)
        dic2=Counter(l2)
        for i in dic1:
            if i in dic2:
                return i
        return -1

        
        