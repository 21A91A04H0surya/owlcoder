class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n=len(nums)
        k=k%n
        d=nums[n-k:n]+nums[0:n-k]
        nums[::]=d
     

        