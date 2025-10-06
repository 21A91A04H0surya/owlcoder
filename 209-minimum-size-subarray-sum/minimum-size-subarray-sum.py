class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        mini=float('inf')
        left=0
        ws=0
        for i in range(len(nums)):
            ws=ws+nums[i]
            if ws<target:
                continue
            else:
                while ws>=target:
                    mini=min(mini,(i+1)-left)
                    ws=ws-nums[left]
                    left+=1
        if mini!=float('inf'):
            return mini
        return 0
        