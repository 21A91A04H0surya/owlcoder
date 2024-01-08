class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        k=set()
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i!=j:
                    if nums[i]+nums[j]==target:
                        k.add(i)
                        k.add(j)
        return list(k)


        