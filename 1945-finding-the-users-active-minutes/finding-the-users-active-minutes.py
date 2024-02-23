class Solution:
    def findingUsersActiveMinutes(self, logs: List[List[int]], k: int) -> List[int]:
        dic={}
        vis=[0 for i in range(k+1)]
        for i in logs:
            if i[0] not in dic:
                dic[i[0]]=[i[1]]
               
            else:
                if i[1] not in dic[i[0]]:
                    dic[i[0]]+=[i[1]]
        for v in dic.values():
            d=len(v)
            vis[d]+=1
        vis.pop(0)
        return vis

        