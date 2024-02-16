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
        for ke,v in d.items():
            if k==0:
                break
            if v==1:
                k-=1
                d[ke]=0
        if k != 0:
            for ke,v in d.items():
                while True:
                    if k ==0 or v==0:
                        break
                    k-=1
                    d[ke]=v-1
                    v=v-1
                if k == 0:
                    break
        c=0
        print(d)
        for k,v in d.items():
            if v!=0:
                c+=1
        return c
        
       
        

        

        

        
