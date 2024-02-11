#User function Template for python3

class Solution:
    def recamanSequence(self, n):
        # codehere
        l=[]
        l.append(0)
        d={}
        for i in range(1,n+1):
            s=l[i-1]-i
            if s not in d and s > 0:
                l.append(l[i-1]-i)
                d[l[i-1]-i]=1
            else:
                l.append(l[i-1]+i)
                d[l[i-1]+i]=1
        return l
                
                
                
        
     
                
                
            
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        
        ob = Solution()
        ans = ob.recamanSequence(n)
        for i in range(n):
            print(ans[i],end=" ")
        print()
# } Driver Code Ends