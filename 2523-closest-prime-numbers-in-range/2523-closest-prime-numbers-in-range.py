class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        se=[1 for i in range(right+1)]
        se[0]=0
        se[1]=0
        cmp=[]
        mindiff=float('inf')
        for i in range(2,len(se)):

            if se[i]==1:
                se[i]=i
                for j in range(i*i,right+1,i):
                    if se[j]==1:
                        se[j]=0
        for i in range(left,right+1):
            if se[i]!=0:
                cmp.append(se[i])
        if len(cmp)==0 or len(cmp)==1:
            return [-1,-1]
        else:
            for i in range(len(cmp)-1):
                j=i+1
                if cmp[j]-cmp[i] < mindiff:
                    a=cmp[i]
                    b=cmp[j]
                    mindiff = cmp[j]-cmp[i]
                    continue
            return [a,b]
