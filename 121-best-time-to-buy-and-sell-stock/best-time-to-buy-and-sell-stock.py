class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minprice=float('inf')
        maxprice=0
        profit=0
        for i in prices:
            if i<minprice:
                minprice=i
                maxprice=0
            else:
                if i > maxprice:
                    if i-minprice>=profit:
                        profit=i-minprice
                        maxprice=i
        return profit
                