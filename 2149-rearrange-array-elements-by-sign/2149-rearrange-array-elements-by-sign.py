class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        p=[]
        n=[]
        for i in nums:
            if i >=0:
                p.append(i)
            else:
                n.append(i)
        o=[]
        for i in range(len(p)):
            o.append(p[i])
            o.append(n[i])
        return o
        
        