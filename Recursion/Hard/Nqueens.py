class Solution:
    def check(self,board,row,col):
        r = row
        c = col 
        while r >= 0 and c >= 0:
            if board[r][c] == 'Q':
                return False
            r -= 1
            c -= 1
        r = row
        c = col 
        while r >= 0:
            if board[r][c] == 'Q':
                return False 
            r -= 1
        r = row 
        c = col 
        while r >= 0 and col < len(board[0]):
            if board[r][c] == 'Q':
                return False 
            r -= 1
            c += 1
        return True 
    
    def poss(self,row,board,ans):
        if row == len(board):
            ans.append( ["".join(r) for r in board] )
            return
        for col in range(len(board[0])):
            if self.check(board, row, col):
                board[row][col] = 'Q'
                self.poss(row + 1, board, ans)
                board[row][col] = '.'
                

    def solveNQueens(self, n):
        board = []
        for i in range(n):
            row = []
            for j in range(n):
                row.append('.')
            board.append(row)
        
        ans = []
        self.poss(0, board, ans)
        return ans