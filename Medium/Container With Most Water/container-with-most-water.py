#User function Template for python3



def maxArea(arr,le):
    #code here
    i=0
    maxi=0
    j=le-1
    while i<=j:
        dist=j-i
        kavi=dist*min(arr[i],arr[j])
        if kavi > maxi:
            maxi = kavi
        if arr[i] == arr[j]:
            i+=1
            j-=1
        elif arr[i] < arr[j]:
            i+=1
        else:
            j-=1
    return maxi
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3



for _ in range(0,int(input())):
    
    n = int(input())
    l = list(map(int,input().split()))
    
    print(maxArea(l,n))
    
    
# } Driver Code Ends