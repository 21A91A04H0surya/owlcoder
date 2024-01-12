//{ Driver Code Starts
// Initial Template for C++
#include <bits/stdc++.h>
using namespace std;

// } Driver Code Ends
//User function Template for C++

class Solution {
  public:
    int unvisitedLeaves(int n, int leaves, int frogs[]) {
        // Code here
        vector<bool>prime;
        prime.assign(leaves+1,false);
        
        for(int i=0;i<n;i++){
            int t=frogs[i];
            if(prime[t]!=true){
                prime[t]=true;
                for(int j=t*2;j<=leaves+1;j+=t){
                    prime[j]=true;
                }
            }
        }
        int cnt=0;
        for(int i=1;i<=leaves;i++){
            if(prime[i]==false){
                cnt+=1;
            }
        }
        return cnt;
    }
};


//{ Driver Code Starts.


int main() {
    int t;
    cin >> t;
    while (t--) {
        int N, leaves;
        cin >> N >> leaves;
        int frogs[N];
        for (int i = 0; i < N; i++) {
            cin >> frogs[i];
        }

        Solution ob;
        cout << ob.unvisitedLeaves(N, leaves, frogs) << endl;
    }
}
// } Driver Code Ends