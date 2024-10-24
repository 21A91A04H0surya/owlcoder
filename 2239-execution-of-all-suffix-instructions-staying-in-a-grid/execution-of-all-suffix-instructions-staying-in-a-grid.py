from typing import List

class Solution:
    def executeInstructions(self, n: int, startpos: List[int], s: str) -> List[int]:
        result = []
        
        # Loop through each starting position in the string
        for i in range(len(s)):
            row, col = startpos  # Reset to the initial position for each starting index
            cnt = 0
            
            # Process commands starting from index i
            for j in range(i, len(s)):
                if s[j] == 'R' and col + 1 < n:
                    col += 1
                    cnt += 1
                elif s[j] == 'L' and col - 1 >= 0:
                    col -= 1
                    cnt += 1
                elif s[j] == 'U' and row - 1 >= 0:
                    row -= 1
                    cnt += 1
                elif s[j] == 'D' and row + 1 < n:
                    row += 1
                    cnt += 1
                else:
                    break  # Stop if move is invalid
            
            # Append the count of valid moves for this starting index
            result.append(cnt)
        
        return result
