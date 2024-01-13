class Solution:
    def minSteps(self, maistr: str, othstr: str) -> int:
        ans=0
        alpha1=[0 for i in range(26)]
        alpha2=[0 for i in range(26)]
        for i in range(len(maistr)):
            d=(ord(maistr[i])-97)
            alpha1[d]+=1
        for i in range(len(othstr)):
            d=(ord(othstr[i])-97)
            alpha2[d]+=1
        for i in range(len(alpha1)):
            if alpha1[i] != 0:
                if alpha2[i] < alpha1[i]:
                    ans+=alpha1[i]-alpha2[i]
        return ans
