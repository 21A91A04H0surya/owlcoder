from collections import Counter
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        dic=Counter(nums)
        nums.clear()
        for k in dic.keys():
            nums.append(k)
        nums=nums
        return len(nums)
        
        
        
        