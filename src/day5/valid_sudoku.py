# 36. Valid Sudoku
# Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

# Each row must contain the digits 1-9 without repetition.
# Each column must contain the digits 1-9 without repetition.
# Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
# Note:

# A Sudoku board (partially filled) could be valid but is not necessarily solvable.
# Only the filled cells need to be validated according to the mentioned rules.


#true 

# board = 
# [["5","3",".",".","7",".",".",".","."]
# ,["6",".",".","1","9","5",".",".","."]
# ,[".","9","8",".",".",".",".","6","."]
# ,["8",".",".",".","6",".",".",".","3"]
# ,["4",".",".","8",".","3",".",".","1"]
# ,["7",".",".",".","2",".",".",".","6"]
# ,[".","6",".",".",".",".","2","8","."]
# ,[".",".",".","4","1","9",".",".","5"]
# ,[".",".",".",".","8",".",".","7","9"]]

#true 

#board[i][j]
# board = 
# [["5","3",".",".","7",".",".",".","."],
#,["6",".",".","1","9","5",".",".","."]]

# def isValidSudoku(board):
#     for i in range(len(board)): 
#         checker = set() 
#         for el in board[i]: 
#             if el != "." and el not in checker:
#                 checker.add(el)
#             elif el !="." and el in checker:
#                 return False 
#     return True 
        
# board = [["5","3",".",".","3",".",".",".","."]
#          ,["6",".",".","1","9","5",".",".","."]]

# # print(isValidSudoku(board))

# # def isValidSudoku(board: list[list[str]]):
# #     #rule: 1. each row, each column, each 3X3 grind has to be within 1-9 number, no repetition 
# #     #i: nested list, o: true/fasle 
    


# #board[i][0]

# def isValidSudoku2(board):
#     #loop through columns
#     for c in range(len(board)): 
#         checker = set() 
#         #loop through rows
#         for r in range(len(board)): 
#             if board[r][c] != "." and board[r][c] not in checker:
#                 checker.add(board[r][c])
#             elif board[r][c] !="." and board[r][c] in checker:
#                 return False 
#     return True 

# board2 = [["5","3"],["6","3"],["6","3"]]

# print(isValidSudoku2(board2))

def isValidSudoku(board: list[list[str]]) -> bool:
    rows = {i : set() for i in range(9)}
    cols = {i : set() for i in range(9)}
    boxes = {i : set() for i in range(9)}
    for r in range(9):
        for c in range(9):
            val = board[r][c]
            if val == '.':
                continue
            val = int(val)
            box = (r // 3) * 3 + c // 3
            if val in rows[r] or val in cols[c] or val in boxes[box]:
                return False
            rows[r].add(val)
            cols[c].add(val)
            boxes[box].add(val)
    return True