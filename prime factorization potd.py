#gfg potd
'''a,b=map(int,input().split())
l=[i for i in range(b+1)]
c=0
for i in range(2,b+1):
    for j in range(i*i,b+1,i):
        if l[j]==j:
            l[j]=i
print(l)

for i in range(a,b+1):
    while i > 1:
        
        c+=1
        i=i//l[i]
        
print(c)'''#1107 testcase passed
#geeks potd
'''from typing import List

class Solution:
    def sumOfPowers(self, a : int, b : int) -> int:
        
        # Calculating smallest prime factors (spf) for every number from 1 to b
        spf = [i for i in range(b+1)]
        for i in range(2, b+1):
            if spf[i] == i:
                for j in range(i*i, b+1, i):
                    if spf[j] == j:
                        spf[j] = i
        
        # Counting all prime factors of each number from a to b
        ans = 0
        for i in range(a, b+1):
            cnt = 0
            while i > 1:
                cnt += 1
                i //= spf[i]
            
            ans += cnt

        return ans'''
