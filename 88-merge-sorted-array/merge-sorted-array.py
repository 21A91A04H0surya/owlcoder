class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # ocnt=nums1.count(0)
        d=len(nums2)
        j=0
        for i in range(len(nums1)):
            if nums1[i]==0:
                if j==d:
                    nums1.sort()
                    return nums1
                else:
                    nums1[i]=nums2[j]
                    j+=1
        nums1.sort()
        return nums1
