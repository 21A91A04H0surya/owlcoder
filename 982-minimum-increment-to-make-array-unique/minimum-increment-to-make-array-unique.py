class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        nums.sort()
        dic={nums[0]:1}
        moves=0
        for i in range(1,len(nums)):
            if nums[i]==nums[i-1]:
                nums[i]=nums[i]+1
                dic[nums[i]]=1
                moves+=1
            else:
                if nums[i] in dic:
                    diff=(nums[i-1]-nums[i])+1
                    moves+=diff
                    nums[i]=nums[i]+diff
                    dic[nums[i]]=1
                else:
                    dic[nums[i]]=1
        return moves
            

        