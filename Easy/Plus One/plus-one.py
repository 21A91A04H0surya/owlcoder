#User function Template for python3

class Solution:
    def increment(self, l, N):
        # code here 
        s=""
        for i in l:
            s+=str(i)
        return str(int(s)+1)
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N=int(input())
        arr=list(map(int,input().split()))
        
        ob = Solution()
        ptr = ob.increment(arr,N)
        for i in ptr:
            print(i,end=" ")
        print()
# } Driver Code Ends