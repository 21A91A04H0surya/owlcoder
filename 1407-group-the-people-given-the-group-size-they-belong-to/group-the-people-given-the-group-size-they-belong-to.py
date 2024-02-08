class Solution:
    def groupThePeople(self, l: List[int]) -> List[List[int]]:
        dic={}
        for i in range(len(l)):
            if l[i] not in dic:
                dic[l[i]]=[i]
            else:
                dic[l[i]]+=[i]
        result=[]
        print(dic)
        for k,v in dic.items():
            if k!=len(v):
                t = k
                for i in range(0,len(v),k):
                    result.append(v[i:k])
                    k+=t
            else:
                result.append(v)
        return result



        