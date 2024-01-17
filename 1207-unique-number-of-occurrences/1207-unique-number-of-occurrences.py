from collections import Counter
class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        dic=Counter(arr)
        l=[]
        for v in dic.values():
            l.append(v)
        d=list(set(l))
        if len(d)==len(l):
            return True
        else:
            return False
        