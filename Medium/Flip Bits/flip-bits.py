#User function Template for python3

class Solution:
    def maxOnes(self, a, n):
        # Your code goes here
        c=0
        for i in range(len(a)):
            if a[i]==1:
                c+=1
                a[i]=-1
            else:
                a[i]=1
        maxi=0
        s=0
        for i in a:
            s+=i
            if s<0:
                s=0
            if s > maxi:
                maxi=s
        return maxi+c
            
        
            
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3

def main():

    T = int(input())

    while(T > 0):
        n = int(input())
        a = [int(x) for x in input().strip().split()]
        ob=Solution()
        print(ob.maxOnes(a, n))

        T -= 1


if __name__ == "__main__":
    main()



# } Driver Code Ends