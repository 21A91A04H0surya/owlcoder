from collections import Counter
class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        dic=Counter(arr1)
        res=[]
        l=[]
        for i in range(len(arr2)):
            if arr2[i] in dic:
                for j in range(dic[arr2[i]]):
                    res.append(arr2[i])
                dic[arr2[i]]=0
        for k,v in dic.items():
            if v!=0:
                while v!=0:
                    l.append(k)
                    v-=1
        l.sort()
        res=res+l
        return res
            
            

        