// # 36. Valid Sudoku
// # Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:
// # Each row must contain the digits 1-9 without repetition.
// # Each column must contain the digits 1-9 without repetition.
// # Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
// # Note:
// # A Sudoku board (partially filled) could be valid but is not necessarily solvable.
// # Only the filled cells need to be validated according to the mentioned rules.
// #true
// # board =
// # [["5","3",".",".","7",".",".",".","."]
// # ,["6",".",".","1","9","5",".",".","."]
// # ,[".","9","8",".",".",".",".","6","."]
// # ,["8",".",".",".","6",".",".",".","3"]
// # ,["4",".",".","8",".","3",".",".","1"]
// # ,["7",".",".",".","2",".",".",".","6"]
// # ,[".","6",".",".",".",".","2","8","."]
// # ,[".",".",".","4","1","9",".",".","5"]
// # ,[".",".",".",".","8",".",".","7","9"]]
// #true
// #board[i][j]
// # board =
// # [["5","3",".",".","7",".",".",".","."],
// #,["6",".",".","1","9","5",".",".","."]]
// # def isValidSudoku(board):
// #     for i in range(len(board)):
// #         checker = set()
// #         for el in board[i]:
// #             if el != "." and el not in checker:
// #                 checker.add(el)
// #             elif el !="." and el in checker:
// #                 return False
// #     return True
// # board = [["5","3",".",".","3",".",".",".","."]
// #          ,["6",".",".","1","9","5",".",".","."]]
var isValidSudoku = function (board) {
  // Check rows, columns, and boards
  const rowSets = Array.from({ length: 9 }, () => new Set());
  const colSets = Array.from({ length: 9 }, () => new Set());
  const boxSets = Array.from({ length: 9 }, () => new Set());
  for (let rowIndex = 0; rowIndex < board.length; rowIndex++) {
    for (let columnIndex = 0; columnIndex < board.length; columnIndex++) {
      const cell = board[rowIndex][columnIndex];
      const boxIndex = Math.floor(rowIndex / 3) * 3 + Math.floor(columnIndex / 3);

      if (cell === ".") continue;
      else if (
        rowSets[rowIndex].has(cell) ||
        colSets[columnIndex].has(cell) ||
        boxSets[boxIndex].has(cell)
      )
        return false;
      else {
        rowSets[rowIndex].add(cell);
        colSets[columnIndex].add(cell);
        boxSets[boxIndex].add(cell);
      }
    }
  }
  return true;
};
// Test with example board
console.log(
  isValidSudoku([
    ["5", "3", ".", ".", "7", ".", ".", ".", "."],
    ["6", ".", ".", "1", "9", "5", ".", ".", "."],
    [".", "9", "8", ".", ".", ".", ".", "6", "."],
    ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
    ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
    ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
    [".", "6", ".", ".", ".", ".", "2", "8", "."],
    [".", ".", ".", "4", "1", "9", ".", ".", "5"],
    [".", ".", ".", ".", "8", ".", ".", "7", "9"],
  ])
);
