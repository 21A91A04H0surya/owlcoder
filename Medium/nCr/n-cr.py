#User function Template for python3

class Solution:
    def pow(self,a,b,mod):
        ans=1
        
        while b:
            if b%2!=0:
                ans=((ans % mod)*(a % mod))
                b-=1
            b=b//2
            a=(a % mod) * (a % mod)
        return ans % mod
    def nCr(self, n, r):
        # code her
        mod=1000000007
        if r>n:
            return 0
        else:
            fact=[]
            infact=[]
            fact.append(1)
            infact.append(1)
            for i in range(1,n+1):
                fact.append(fact[-1]*i)
                fact[i]%=mod
                infact.append(self.pow(fact[i],mod-2,mod))
            # print(fact[n]//(fact[n-r]*fact[r]))
            a=((fact[n]%mod)*(infact[r]%mod)*(infact[n-r]%mod))%mod
            return a


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import sys
sys.setrecursionlimit(10**6)

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n, r = [int(x) for x in input().split()]
        
        ob = Solution()
        print(ob.nCr(n, r))
# } Driver Code Ends