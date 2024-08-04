class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        l=[]
        for i in range(0,len(nums)):
            for j in range(i+1,len(nums)+1):
                d=nums[i:j]
                l.append(sum(d))
        l.sort()
        su=sum(l[left-1:right])
        print(l)
        return su%((10**9)+7)
        