class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        tokens.sort()
        maxi=0
        score=0
        if len(tokens)==0:
            return 0

        elif len(tokens)==1:
            if tokens[0] > power:
                return 0
            return 1
        else:
            i=0
            j=len(tokens)-1
            while i!=j:
                # if i == j and tokens[i]<=power:
                #     score+=1
                #     maxi=max(maxi,score)
                #     break
                
                    
                if tokens[i] <= power:
                    score+=1
                    maxi=max(maxi,score)
                    power=power-tokens[i]
                    i+=1
                elif tokens[i] > power and score!=0:
                    score-=1
                    power=power+tokens[j]
                    j-=1
                else:
                    return maxi
            if tokens[i] <= power:
                score+=1
                maxi=max(maxi,score)
            return maxi

                



        