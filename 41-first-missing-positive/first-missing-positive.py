class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        dic1={}
        dic2={}
        for i in range(1,len(nums)+1):
            dic1[i]=1
        for i in nums:
            if i in dic1:
                dic1[i]=0
        for k,v in dic1.items():
            if v==1:
                return k
        return max(nums)+1 
        
        