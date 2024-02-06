       
class Solution:
            def groupAnagrams(self, s: List[str]) -> List[List[str]]:
                dic={}
                for i in s:
                    v=''.join(sorted(i))
                    if v not in dic:
                        dic[v]=[i]
                    else:
                        dic[v]+=[i]
                return dic.values()

              
                            
        