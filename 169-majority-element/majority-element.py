from collections import Counter
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        d=Counter(nums)
        n=len(nums)
        for k , v in d.items():
            if v>(n//2):
                return k
                break
