class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        d=nums.count(val)
        for i in range(d):
            nums.remove(val)
        