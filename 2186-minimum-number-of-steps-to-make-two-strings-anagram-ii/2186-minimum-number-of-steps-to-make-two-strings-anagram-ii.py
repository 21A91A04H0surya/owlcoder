class Solution:
    def minSteps(self, s: str, t: str) -> int:
        l1=[0]*26
        l2=[0]*26
        for i in s:
            d=ord(i)-97
            l1[d]+=1
        for i in t:
            d=ord(i)-97
            l2[d]+=1
        ans=0
        for i in range(len(l1)):
            ans+=abs(l1[i]-l2[i])
        return ans
        