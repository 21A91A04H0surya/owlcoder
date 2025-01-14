from collections import Counter
class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        dic=Counter(A)
        overallcnt=0
        result=[]
        for k,v in dic.items():
            dic[k]=0
        for i in range(len(A)):
            dic[A[i]]+=1
            dic[B[i]]+=1
            if dic[A[i]]==2:
                overallcnt+=1
                dic[A[i]]=0
            if dic[B[i]]==2:
                overallcnt+=1
                dic[B[i]]=0
                
            result.append(overallcnt)
        return result
            


        