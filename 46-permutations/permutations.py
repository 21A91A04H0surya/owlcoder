# from itertools import permutations
class Solution:
    def printpermutations(self,nums,frq,p, l):
       
        if len(p)==len(nums):
            c = p.copy()
            l.append(c)
            return 
        else:
            for i in range(len(nums)):
                if frq[i]==0:
                    frq[i]=1
                    p.append(nums[i])
                    self.printpermutations(nums,frq,p, l)
                    p.pop()
                    frq[i]=0
    def permute(self, nums: List[int]) -> List[List[int]]:
      
        ans=[0]*len(nums)
        l=[]
        p=[]
        self.printpermutations(nums,ans,p, l)
        print(l)
        return l
        
        
        
        
        