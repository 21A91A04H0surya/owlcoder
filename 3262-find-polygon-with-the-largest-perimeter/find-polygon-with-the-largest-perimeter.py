class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        pf=[]
        nums.sort()
        s=0
        maxi=-1
        for i in nums:
            s+=i
            pf.append(s)
        for i in range(2,len(nums)):
            if nums[i]<pf[i-1]:
                maxi=pf[i]
        return maxi
            
            
        

        


        
        