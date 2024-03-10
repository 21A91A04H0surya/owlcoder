from collections import Counter
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        d=Counter(nums2)
        dic={}
        for i in nums1:
            if i in d and i not in dic:
                dic[i]=1
        return list(dic.keys())