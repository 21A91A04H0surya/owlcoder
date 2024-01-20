#User function Template for python3

class Solution:
	def pushZerosToEnd(self,l, n):
    	# code here
    	oc=0
    	stack=[]
    	for i in l:
    	    if i!=0:
    	        stack.append(i)
    	    else:
    	        oc+=1
    	l1=[0]*oc
    	d=stack+l1
    	l[::]=d[::]


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ob.pushZerosToEnd(arr, n)
        for x in arr:
            print(x, end=" ")
        print()
        tc -= 1
# } Driver Code Ends