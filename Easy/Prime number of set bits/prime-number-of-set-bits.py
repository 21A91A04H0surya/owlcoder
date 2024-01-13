#User function Template for python3
import math
class Solution:
    
	def primeSetBits(self,l,r):
	    def prim(i):
            if i==1:
                return False
            sq=int(math.sqrt(i))
            for j in range(2,sq+1):
                if i%j==0:
                    return False
            return True
	    
	    def countset_bits(n):
	        c=0
	        while n:
	            if n & 1 >0:
	                c+=1
	            n=n>>1
	        return c
		# code here
		cnt=0
		for i in range(l,r+1):
		    d=countset_bits(i)
		    
		    if prim(d):
		        cnt+=1
	    return cnt
		        



#{ 
 # Driver Code Starts
#Initial Template for Python 3

#Initial Template for Python 3
if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		L,R = input().split()
		L=int(L)
		R=int(R)
		ob = Solution();
		print(ob.primeSetBits(L,R))

# } Driver Code Ends