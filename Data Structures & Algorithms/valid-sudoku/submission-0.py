class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row in board:
            if len(set(row) - set(['.'])) != (9 - row.count('.')):
                return False
        for i in range(len(board)):
            column = [row[i] for row in board]
            if len(set(column) - set(['.'])) != (9 - column.count('.')):
                return False
        for i in range(len(board)):
            m = i // 3
            n = i % 3
            square = [board[k][j] for k in range(3 * m, 3 * m + 3) for j in range(3 * n, 3 * n + 3)]
            if len(set(square) - set(['.'])) != (9 - square.count('.')):
                return False

        return True
        