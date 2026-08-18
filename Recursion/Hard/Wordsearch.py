class Solution:
    def possible(self, i, j, k, board, word):
        if k == len(word):
            return True
        if i < 0 or j < 0 or j >= len(board[0]) or i >= len(board) or word[k] != board[i][j]:
            return False
        temp = board[i][j]
        board[i][j] = ' '
        ans = ( self.poss(board, word, i-1,j,k+1) or
                self.poss(board, word, i+1,j,k+1) or
                self.poss(board, word, i,j-1,k+1) or
                self.poss(board, word, i,j+1,k+1) )
        board[i][j] = temp 
        return ans
        
    def exist(self, board, word):
        for row in range(len(board)):
            for col in range(len(board[0])):
                if board[row][col] == word[0]:
                    if self.possible(row, col, 0, board, word):
                        return True 
        return False