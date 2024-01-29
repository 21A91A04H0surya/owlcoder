from collections import Counter
class Solution:
    def findExtra(self,a,b,n):
        #add code here
        d=Counter(b)
        for i in range(len(a)):
            if a[i] not in d:
                return i
        
                
                


#{ 
 # Driver Code Starts
if __name__ == "__main__":
    t=int(input())
    for i in range(t):
        n=int(input())
        a=list(map(int,input().split()))
        b=list(map(int,input().split()))
        print(Solution().findExtra(a,b,n))
# } Driver Code Ends