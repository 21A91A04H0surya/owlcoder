class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxi=float('-inf')
        dic={}
        left=0
        for i in range(len(s)):
            if s[i] not in dic:
                dic[s[i]]=i 
                maxi=max(maxi,i-left+1)
            else:
                left = max(left, dic[s[i]] + 1)
                dic[s[i]]=i
                maxi=max(maxi,i-left+1)
        if maxi!=float('-inf'):
            return maxi
        return 0
