#User function Template for python3

class Solution:
    def DivisibleByEight(self,s):
        if len(s)<3:
            if int(s)%8==0:
                return 1
            return -1
        s1=""
        s1=s1+s[-3]
        s1=s1+s[-2]
        s1=s1+s[-1]
        s1=int(s1)
        if s1%8==0:
            return 1
        return -1
            
        
            


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__=='__main__':
    t=int(input())
    for _ in range(t):
        S=input()
        ob=Solution()
        print(ob.DivisibleByEight(S))
# } Driver Code Ends