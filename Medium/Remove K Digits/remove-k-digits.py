#User function Template for python3

class Solution:

    def removeKdigits(self, s,k):
        stack=[]
        c=k
        # code here
        if len(s) <k :
            return 0
        else:
            for i in range(len(s)):
                if len(stack)==0:
                    stack.append(s[i])
                elif s[i] >= stack[-1]:
                    stack.append(s[i])
                else:
                    while True:
                        if c==0 or len(stack)==0 or stack[-1]<=s[i]:
                            break
                        if stack[-1]>s[i]:
                            stack.pop()
                            c-=1
                    stack.append(s[i])
            while c:
                stack.pop()
                c-=1
            st = "".join(stack).lstrip("0")
            if len(st)==0:
                return 0
            else:
                return st
                
                    
            
                
            
                
            
            
            
            


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':

    t = int(input())

    for _ in range(t):
        S = input()
        K = int(input())

        obj = Solution()

        ans = obj.removeKdigits(S, K)

        print(ans)


# } Driver Code Ends