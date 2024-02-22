from collections import Counter
class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        d=Counter(nums)
        for i in d:
            if i==target:
                return True
        return False
        