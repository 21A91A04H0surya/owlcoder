#User function Template for python3

class Solution:
    def nthCharacter(self, s, r, n):
        # code here
        result=""
        while r!=0:
            if len(result)!=0:
                s=result
                result=""

            for i in range(n+1):
                if s[i]=='1':
                    result+='10'
                    
                else:
                    result+='01'
            # print(result)
            r-=1
       
        return result[n]
                
                


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        snr = input().split()
        S, R, N = snr[0], int(snr[1]), int(snr[2])
        ob = Solution()
        print(ob.nthCharacter(S, R, N))
# } Driver Code Ends