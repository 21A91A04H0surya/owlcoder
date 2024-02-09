from collections import Counter
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        c=0
        d=Counter(nums)
        l=[]
        for k,v in d.items():
            if v > 2:
                c=c+(v-2)
                l.append(k)
                l.append(k)
            elif v == 1:
                l.append(k)
            else:
                l.append(k)
                l.append(k)
        nums[::]=l[::]
        return len(nums)

        