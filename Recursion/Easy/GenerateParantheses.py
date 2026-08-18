class Solution:
    def backtrack(self, open, close, n, current, ans):
        if open > n:
            return 
        if open == n and close == n:
            ans.append(current)
            return
        if open < n:
            self.backtrack(open + 1, close, n, current + "(", ans)
        if close < open:
            self.backtrack(open, close + 1, n, current + ")", ans)
            
    def generateParanthesis(self, n):
        ans = []
        self.backtrack(0, 0, n, "", ans)
        return ans