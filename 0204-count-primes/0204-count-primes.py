class Solution:
    def countPrimes(self, n: int) -> int:
        if n==1 or n==0:
            return 0
        else:
            pri_count=0
            se=[1 for i in range(n)]
            se[0]=0
            se[1]=0
            for i in range(2,n):
                if se[i]==1:
                    pri_count+=1
                    for j in range(i*i,n,i):
                        se[j]=0
            return pri_count
          
            
            
            
        