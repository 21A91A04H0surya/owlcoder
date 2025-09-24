class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        s=[]
        for i in range(len(prices)):
            c=0
            for j in range(i+1,len(prices)):
                if prices[j]<=prices[i]:
                    s.append(prices[i]-prices[j])
                    c+=1
                    break
            if c==0:
                s.append(prices[i])
        return s
            

        