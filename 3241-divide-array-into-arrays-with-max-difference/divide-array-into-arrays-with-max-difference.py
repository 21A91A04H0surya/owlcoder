class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        nums.sort()
        l=[]
        c=0
        d=3
        for i in range(0,len(nums),3):
            l.append(nums[i:d])
            d+=3
        d=len(l)
        for i in l:
            if abs(i[0]-i[-1])>k:
                return[]
        else:
            return l