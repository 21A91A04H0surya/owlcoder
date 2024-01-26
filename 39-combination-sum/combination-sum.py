class Solution:
    def combinations(self,ind,arr,tar,n,d,o):
        if ind == n:
            if tar == 0:
                f=d.copy()
                o.append(f)
            return 
        #pick
        if arr[ind] <= tar:
            d.append(arr[ind])
            tar=tar-arr[ind]
            self.combinations(ind,arr,tar,n,d,o)
            tar=tar+arr[ind]
            d.pop()
            #non pick
        self.combinations(ind+1,arr,tar,n,d,o)        
    def combinationSum(self, arr: List[int], tar: int) -> List[List[int]]:
        n=len(arr)
        d=[]
        o=[]
        self.combinations(0,arr,tar,n,d,o)
        return o
        
        
        