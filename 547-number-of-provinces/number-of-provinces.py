class Solution:
    def fun(self,ind,visited,l):
        if visited[ind]==0:
            t=l[ind]
            visited[ind]=1
            for i in t:
                if visited[i]==0:
                    self.fun(i,visited,l)
    def findCircleNum(self, arr: List[List[int]]) -> int:
        l=[]
        l.append([])
        for i in arr:
            o=[]
            for j in range(len(i)):
                if i[j]==1:
                    o.append(j+1)
            l.append(o)
        c=0
        visited=[0 for i in range(len(arr)+1)]
        for i in range(1,len(arr)+1):
            if visited[i]==0:
                c+=1
                self.fun(i,visited,l)
        return c

        