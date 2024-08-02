class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        swaps=0
        for i in nums:
            if i%3==0:
                continue
            else:
                if (i-1)%3==0:
                    swaps+=1
                elif (i+1)%3==0:
                    swaps+=1
        return swaps
                
                

        