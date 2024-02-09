from collections import Counter

class Solution:
    def search(self, pat, lst):
        l = Counter(pat)
        c = 0
        n = len(pat)
        window = Counter(lst[:n])  # Initialize the Counter for the initial window
        if window == l:  # Check if the initial window matches the pattern
            c += 1
        for i in range(1, len(lst) - n + 1):  # Iterate through the list
            window[lst[i - 1]] -= 1  # Remove the leftmost element from the window
            if window[lst[i - 1]] == 0:  # If the count becomes zero, remove the key
                del window[lst[i - 1]]
            window[lst[i + n - 1]] += 1  # Add the rightmost element to the window
            if window == l:  # Check if the updated window matches the pattern
                c += 1
        return c

	        


#{ 
 # Driver Code Starts
#Initial Template for Python 3


# Driver code 
if __name__ == "__main__": 		
    tc=int(input())
    while tc > 0:
        txt=input().strip()
        pat=input().strip()
        ob = Solution()
        ans = ob.search(pat, txt)
        print(ans)
        tc=tc-1
# } Driver Code Ends