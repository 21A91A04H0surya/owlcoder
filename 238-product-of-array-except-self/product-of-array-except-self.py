from collections import Counter
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        d=Counter(nums)
        s=1
        if d[0]==1:
            for i in nums:
                if i!=0:
                    s=s*i
            for i in range(len(nums)):
                if nums[i]==0:
                    nums[i]=s
                else:
                    nums[i]=0
        elif d[0]>=2:
            for i in range(len(nums)):
                nums[i]=0
        else:
            s=1
            for  i in nums:
                s=s*i
            for i in range(len(nums)):
                nums[i]=s//nums[i]
        return nums

        
        