class Solution:
    def fib(self, n: int) -> int:
        f0=0
        f1=1
        l=[0,1]
        if n==0:
            return 0
        else:
            
            for i in range(2,n+1):
                l.append(l[i-1]+l[i-2])
            print(l)
            return l[-1]
            
            
        