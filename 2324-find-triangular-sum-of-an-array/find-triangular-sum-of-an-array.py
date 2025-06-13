class Solution:
    def fun(self,l):
        if len(l)==1:
            return l[0]
        for i in range(0,len(l)-1):
            l[i]=((l[i]+l[i+1])%10)
        
        l.pop()
        return self.fun(l)
    def triangularSum(self, nums: List[int]) -> int:
        return self.fun(nums)
        