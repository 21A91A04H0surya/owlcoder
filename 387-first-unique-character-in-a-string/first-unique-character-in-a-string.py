from collections import Counter
class Solution:
    def firstUniqChar(self, s: str) -> int:
        dic=Counter(s)
        tar=0
        for k,v in dic.items():
            if v==1:
                tar=k
                break
        for i in range(len(s)):
            if s[i]== tar:
                return i
        return -1
        


            
        