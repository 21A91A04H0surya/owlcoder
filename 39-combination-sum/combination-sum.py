class Solution:
    def fun(self,ind,la,arr,o,ans,tar):
        if ind>=la:
            if tar==0:
                a=o.copy()
                print(a)
                ans.append(a)
            return
        # if(arr[ind] > tar): return
        '''if pick'''
        if(arr[ind] <= tar):
            o.append(arr[ind])
            self.fun(ind,la,arr,o,ans,tar-arr[ind])
            o.pop()
        '''non pick'''
        self.fun(ind+1,la,arr,o,ans,tar)
    def combinationSum(self, arr: List[int], tar: int) -> List[List[int]]:
        ans=[]
        o=[]
        m=len(arr)
        self.fun(0,m,arr,o,ans,tar)
        return ans

        