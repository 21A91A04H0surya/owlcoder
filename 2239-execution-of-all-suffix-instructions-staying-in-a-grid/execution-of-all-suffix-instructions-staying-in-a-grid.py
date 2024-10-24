from typing import List

class Solution:
    def executeInstructions(self, n: int, startpos: List[int], s: str) -> List[int]:
        result = []
        
        # Directions mapping
        directions = {
            'R': (0, 1),
            'L': (0, -1),
            'U': (-1, 0),
            'D': (1, 0)
        }
        
        for i in range(len(s)):
            row, col = startpos  # Start from the initial position
            cnt = 0
            
            for j in range(i, len(s)):
                dr, dc = directions[s[j]]
                new_row, new_col = row + dr, col + dc
                
                # Check if the new position is within bounds
                if 0 <= new_row < n and 0 <= new_col < n:
                    row, col = new_row, new_col
                    cnt += 1
                else:
                    break
            
            result.append(cnt)
        
        return result
