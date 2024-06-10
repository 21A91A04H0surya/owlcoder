class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        i=0
        j=len(nums)-1
        li=[]
        while i<j:
            if nums[i]==0:
                li.append(i)
            if nums[j]==0:
                li.append(j)
            i+=1
            j-=1
        if i==j and nums[i]==0:
            li.append(i)
        if len(li)!=0:
            li.sort()
            maxcnt=0
            var=max(((len(nums)-1) - li[-1]),li[0])
            for i in range(len(li)-1):
                d=li[i+1]-li[i]-1
                var=max(var,d)
            return var
        return len(nums)