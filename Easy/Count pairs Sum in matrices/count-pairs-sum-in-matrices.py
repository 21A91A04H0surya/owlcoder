#User function Template for python3
class Solution:
	def countPairs(self, mat1, mat2, n, x):
	    l1=[]
	    l2=[]
	    c=0
	    

	    for i in range(n):
	        for j in range(n):
	            l1.append(mat1[i][j])
	            l2.append(mat2[i][j])
	    i=0
	    j=len(l1)-1
	    while True:
	        if i>len(l1)-1 or j<0:
	            break
	        if l1[i]+l2[j]==x:
	            c+=1
	            i+=1
	            j-=1
	        elif l1[i]+l2[j]>x:
	            j-=1
	        else:
	            i+=1
	    return c
		


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n , x = input().split()
		n,x = int(n), int(x)
		mat1 = []
		for _ in range(n):
			a = [int(x) for x in input().split()]
			mat1.append(a)

		mat2 = []
		for _ in range(n):
			a = [int(x) for x in input().split()]
			mat2.append(a)

		ob = Solution()
		ans = ob.countPairs(mat1, mat2, n, x)
		print(ans)

# } Driver Code Ends