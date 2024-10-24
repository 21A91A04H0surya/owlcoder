from typing import List
class Solution:
    def executeInstructions(self, n: int, startpos: List[int], s: str) -> List[int]:
        result=[]
        for i in range(len(s)):
            cnt=0
            row,col=startpos[0],startpos[1]
            for j in range(i,len(s)):
                if s[j]=='R' and col+1<n:
                    cnt+=1
                    col+=1
                elif s[j]=='L' and col-1>=0:
                    col-=1
                    cnt+=1
                elif s[j]=='U' and row-1>=0:
                    cnt+=1
                    row-=1
                elif s[j]=='D' and row+1<n:
                    row+=1
                    cnt+=1
                else:
                    break
            result.append(cnt)
        return result