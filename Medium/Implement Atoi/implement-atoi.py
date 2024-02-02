#User function template for Python

class Solution:
    # your task is to complete this function
    # function should return an integer
    def atoi(self,s):
        c=0
        for i in range(len(s)):
            if i==0:
                if s[i]=='-':
                    c=1
            else:
                if ord(s[i])<48 or ord(s[i])>57:
                    return -1
        return int(s)
            
                
                
            


#{ 
 # Driver Code Starts
#Initial template for Python

if __name__=='__main__':
    t=int(input())
    for i in range(t):
        string = input().strip();
        ob=Solution()
        print(ob.atoi(string))
# } Driver Code Ends