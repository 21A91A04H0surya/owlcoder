import heapq
class Solution:
    def furthestBuilding(self, l: List[int], bricks: int, ladders: int) -> int:
        
        q=[]
        for i in range(len(l) - 1):
            dif = l[i + 1] - l[i]
            if(dif > 0):
                heapq.heappush(q, -dif)
                bricks -= dif
                if(bricks < 0 and ladders > 0):
                    ladders -= 1
                    bricks += -heapq.heappop(q)
    
            if(bricks < 0 and ladders <= 0): return i
        return len(l) - 1
        
        

         
        