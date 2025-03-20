from typing import List
from collections import defaultdict

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        rows = defaultdict(set)  # Hash Map to check row duplicates
        cols = defaultdict(set)   # Hash Map to check column duplicates
        squares = defaultdict(set) # Hash to check duplicates in 3 x 3 grids

        for r in range(9):
            for c in range(9):

                if board[r][c] == ".":
                    continue

                if (board[r][c] in rows[r]
                    or board[r][c] in cols[c]
                    or board[r][c] in squares[(r // 3, c // 3)]):  # This means a duplicate is found
                    return False
                
                rows[r].add(board[r][c])
                cols[c].add(board[r][c])
                squares[(r // 3, c // 3)].add(board[r][c]) # If not a duplicate add it to each of the hashes
        return True