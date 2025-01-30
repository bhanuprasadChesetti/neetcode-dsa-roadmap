

# Problem: https://neetcode.io/problems/valid-sudoku

from typing import List
from math import sqrt
from collections import defaultdict

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
       
        
        board_length = len(board)

        box_length = int(sqrt(board_length))

        rows = defaultdict(set)

        cols = defaultdict(set)

        boxes = defaultdict(dict)


        for i in range(board_length):
            for j in range(board_length):

                num = board[i][j]

                if num == '.':
                    continue
                

                # Checking duplicates in Row
                if num in rows[i]:
                    return False
                

                # Checking duplicates in Column
                if num in cols[j]:
                    return False
                
                # Checking duplicates in box (i,e 3*3 for board length of 9)
                x,y = (i//box_length),(j//box_length)

                boxes[x][y] = boxes[x].get(y,set())

                if num in boxes[x][y]:
                    return False

                rows[i].add(num)
                cols[j].add(num)
                boxes[x][y].add(num)

        
        return True
                     


