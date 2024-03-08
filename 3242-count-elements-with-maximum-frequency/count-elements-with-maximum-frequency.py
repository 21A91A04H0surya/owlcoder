from collections import Counter
class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        d=Counter(nums)
        c=0
        maxi=max(d.values())
        for i in nums:
            if d[i]==maxi:
                c+=1
        return c
        