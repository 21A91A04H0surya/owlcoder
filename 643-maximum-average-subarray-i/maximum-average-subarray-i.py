class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        ws=sum(nums[:k])
        maxi=ws
        for i in range(k,len(nums)):
            ws=ws+nums[i]-nums[i-k]
            maxi=max(ws,maxi)
        return maxi/k



                        
            


        