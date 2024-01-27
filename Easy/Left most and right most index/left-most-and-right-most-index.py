#User function Template for python3

class Solution:
    def indexes(self, l, x):
        # Your code goes here
        ans=[]
        i=0
        j=len(l)-1
        while i<=j:
            if l[i]==x and l[j]==x:
                ans.append(i)
                ans.append(j)
                return ans
                
                
            elif l[i]!=x and l[j]!=x:
                i+=1
                j-=1
            elif l[i]==x and l[j]!=x:
                j-=1
            elif l[i]!=x and l[j]==x:
                i+=1
        return [-1,-1]
            
                
            
       
    
            
        
    


#{ 
 # Driver Code Starts
#Initial Template for Python 3

def main():

    T = int(input())

    while(T > 0):
        n = int(input())
        a = [int(x) for x in input().strip().split()]
        k = int(input())
        obj = Solution()
        ans = obj.indexes(a, k)
        if ans[0]==-1 and ans[1]==-1:
            print(-1)
        else:
            print(ans[0], end=' ')
            print(ans[1])

        T -= 1


if __name__ == "__main__":
    main()


# } Driver Code Ends