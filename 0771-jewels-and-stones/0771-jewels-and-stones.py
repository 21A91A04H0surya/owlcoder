from collections import Counter
class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        d1=Counter(stones)
        ans=0
        for i in jewels:
            for k ,v in d1.items():
                if k==i:
                    ans+=v
        return ans
                
                
                
        
        