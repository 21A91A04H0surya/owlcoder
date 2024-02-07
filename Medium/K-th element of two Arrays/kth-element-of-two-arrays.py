#User function Template for python3

class Solution:
    def kthElement(self,  arr1, arr2, n, m, k):
        l=arr1+arr2
        l.sort()
        low=0
        high=len(l)-1
        k-=1
        while low <= high:
            if low==k:
                return (l[low])
                break
            elif high == k:
                return (l[high])
                break
            mid = (low+high)//2
            if mid == k :
                return l[mid]
                break
            if mid > k:
                high = mid - 1
            else:
                low= mid + 1
        
        
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3

def main():

    T = int(input())

    while(T > 0):
        sz = [int(x) for x in input().strip().split()]
        n, m, k = sz[0], sz[1], sz[2]
        a = [int(x) for x in input().strip().split()]
        b = [int(x) for x in input().strip().split()]
        ob = Solution()
        print(ob.kthElement( a, b, n, m, k))

        T -= 1


if __name__ == "__main__":
    main()

# } Driver Code Ends