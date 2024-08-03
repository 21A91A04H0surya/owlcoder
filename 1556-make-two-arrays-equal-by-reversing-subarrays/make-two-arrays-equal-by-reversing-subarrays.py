from collections import Counter
class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        dic1=Counter(target)
        dic2=Counter(arr)
        if dic1==dic2:
            return True
        return False
        