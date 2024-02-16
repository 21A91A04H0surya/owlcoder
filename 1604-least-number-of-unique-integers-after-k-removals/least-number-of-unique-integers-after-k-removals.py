from collections import Counter
class Solution:
    def findLeastNumOfUniqueInts(self, nums: List[int], k: int) -> int:
        d=Counter(nums)
        arr = sorted(nums, key=lambda x: (d[x], -x))
        print(arr)
        d={}
        for i in arr:
            if i not in d:
                d[i]=1
            else:
                d[i]+=1
        c=0
        print(d)
        for ke,v in d.items():
            if k==0:
                break
            if v <= k:
                c+=1
                k=k-v
            else:
                break
        return len(d)-c

    
        
       
        

        

        

        
