#User function Template for python3

class Solution:
    #Function to return the position of the first repeating element.
    def firstRepeated(self,arr, n):
        d={}
        ia=999999
        for i in range(len(arr)):
            if arr[i] not in d:
                d[arr[i]]=i
            else:
                ia=min(ia,d[arr[i]])
                
        if ia==999999:
            return -1
        return ia+1
                
        
        #arr : given array
        #n : size of the array


#{ 
 # Driver Code Starts
#Initial Template for Python 3

#contributed by RavinderSinghPB
if __name__=='__main__':
    t=int(input())
    for _ in range(t):
        n=int(input())
        
        arr=[int(x) for x in input().strip().split()]
        ob = Solution()
        print(ob.firstRepeated(arr, n))
# } Driver Code Ends