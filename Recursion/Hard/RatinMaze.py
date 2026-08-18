class Solution:
    def __init__(self):
        self.result = []
    def path(self, row, col, dir, mat, n):
        if row == n - 1 and col == n - 1:
            self.result.append(dir)
            return 
        if mat[row][col] == 0:
            return 
        mat[row][col] = 0
        if row - 1 >= 0 and mat[row - 1][col] == 1:
            self.path(row - 1, col, dir + "U", mat, n)
        if col - 1 >= 0 and mat[row][col - 1] == 1:
            self.path(row, col - 1, dir + "L", mat, n)
        if row < n - 1 and mat[row + 1][col] == 1:
            self.path(row + 1, col, dir + "D", mat, n)
        if col + 1 < n and mat[row][col + 1] == 1:
            self.path(row - 1, col, dir + "R", mat, n)
        mat[row][col] = 1
        
    def findpath(self, grid):
        n = len(grid)
        self.result = []
        if grid[0][0] == 0 or grid[n - 1][n - 1] == 0:
            return self.result
        self.path(0, 0, "", grid, n)
        self.result.sort()
        return self.result 
        
        