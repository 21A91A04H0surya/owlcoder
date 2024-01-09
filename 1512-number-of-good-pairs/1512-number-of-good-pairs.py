class Solution:
    def numIdenticalPairs(self, l: List[int]) -> int:
        i=0
        j=1
        c=0
        for i in range(len(l)):
            for j in range(i+1,len(l)):
                if l[i]==l[j] and i < j:
                    c+=1
        return c
        