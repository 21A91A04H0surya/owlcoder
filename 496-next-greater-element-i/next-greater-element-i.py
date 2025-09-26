from collections import Counter
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res=[]
        dic=Counter(nums2)
        for i in nums1:
            if i in dic:
                x=nums2.index(i)
                l=nums2[x+1:]
                for j in l:
                    if j > i:
                        res.append(j)
                        break
                else:
                    res.append(-1)
        return res

        