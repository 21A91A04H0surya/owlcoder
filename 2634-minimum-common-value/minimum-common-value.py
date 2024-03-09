class Solution:
    def getCommon(self, l1: List[int], l2: List[int]) -> int:
        while len(l1)> 0 and len(l2)>0:
            if l1[0]==l2[0]:
                return l1[0]
            elif l1[0]>l2[0]:
                l2.pop(0)
            else:
                l1.pop(0)
        return -1
        
        