#User function Template for python3

#Back-end complete function Template for Python 3


class Solution:
    def sriram(self,i):
        s=0
        while i:
            s+=i%10
            i=i//10
        return s
            
    def RulingPair(self, arr, n): 
    	# Your code goes here
    	dic={}
    	for i in arr:
    	    d=self.sriram(i)
    	    if d not in dic:
    	        dic[d]=[i]
    	    else:
    	        dic[d]+=[i]
        maxi=0
        for k,v in dic.items():
            if len(v)> 1:
                v.sort()
                o=v[-1]+v[-2]
                if o > maxi:
                    maxi=o
        if maxi==0:
            return -1
        return maxi
    	        



#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        obj = Solution();
        print(obj.RulingPair(arr,n))



# } Driver Code Ends