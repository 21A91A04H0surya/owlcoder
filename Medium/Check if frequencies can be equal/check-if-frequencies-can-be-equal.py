#User function Template for python3
from collections import Counter
class Solution:
    def sameFreq(self, s):
        # code here
        c=1
        d=Counter(s)
        dif=list(d.values())
        dif.sort()
        if len(dif)==2 and (dif[0]==dif[-1] or abs(dif[0]-dif[-1])==1):
            return 1
        else:
            dic=Counter(dif)
           
            if len(dic)==2:
               
                l1=list(dic.keys())
                l1.sort()
                if l1[0]==1:
                    return 1
                return 0
            else:
                mini=min(dif)
                for i in dif:
                    if i==mini:
                        continue
                    else:
                        c=c-abs(i-mini)
                        if c < 0:
                            return 0
            return 1
                


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == "__main__":
	T=int(input())

	for _ in range(T):
		s = input()
		ob = Solution()
		answer = ob.sameFreq(s)
		if answer:
			print(1)
		else:
			print(0)

# } Driver Code Ends