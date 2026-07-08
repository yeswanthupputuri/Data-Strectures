class Solution:
    def celebrity(self, M):
        n = len(M)
        top = 0
        bottom = n - 1
        while top < bottom:
            if M[top][bottom] == 1:
                top += 1
            elif M[bottom][top] == 1:
                bottom -= 1
            else:
                top += 1
                bottom -= 1
        if top > bottom:
            return -1
        for i in range(n):
            if i != top and (M[top][i] == 1 or M[i][top] == 0):
                return -1
        return top