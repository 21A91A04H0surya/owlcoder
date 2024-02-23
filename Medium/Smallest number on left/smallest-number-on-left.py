# User function Template for Python3

class Solution:
    def leftSmaller(self, n, a):
        # code here
        stack=[]
        res=[]
        c=0

        res.append(-1)
        stack.append(a[0])
        for i in range(1,n):
            if len(stack)==0:
                stack.append(a[i])
            else:
                while stack[-1] >= a[i]:
                    stack.pop()
                    if len(stack)==0:
                        c=1
                        break
                if c ==1:
                    res.append(-1)
                    stack.append(a[i])
                    c=0
                else:
                    res.append(stack[-1])
                    stack.append(a[i])
        return res
                
                    
                    
                
                
    

                    
            
            


#{ 
 # Driver Code Starts
# Initial Template for Python3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        a = input().split()
        for i in range(n):
            a[i] = int(a[i])
        
        ob = Solution()
        ans = ob.leftSmaller(n, a)
        for u in(ans):
            print(u,end = " ")
        print()
# } Driver Code Ends