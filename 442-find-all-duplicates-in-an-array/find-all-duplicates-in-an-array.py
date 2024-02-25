from collections import Counter
class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        l=[]
        dictionary=Counter(nums)
        for key,value in dictionary.items():
            if value > 1:
                l.append(key)
        return l

        