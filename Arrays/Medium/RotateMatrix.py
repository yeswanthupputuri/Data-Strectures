class Solution:
    def rotatematrix(self, matrix):
        n = len(matrix)
        for i in range(0, n-1):
            for j in range(i+1, n):
                matrix[i][j],matrix[j][i] = matrix[j][i], matrix[i][j]
        for i in range(n):
            left = 0
            right = n - 1
            while left < right:
                matrix[i][left],matrix[i][right] = matrix[i][right], matrix[i][left]
                left += 1
                right -= 1
            return matrix