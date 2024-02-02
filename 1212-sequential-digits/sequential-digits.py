class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        s="123456789"
        o=[]
        for i in range(len(s)):
            for j in range(i+1,len(s)+1):
                d=s[i:j]
                if int(d)>= low and int(d) <=high :
                    o.append(int(d))
        return sorted(o)      