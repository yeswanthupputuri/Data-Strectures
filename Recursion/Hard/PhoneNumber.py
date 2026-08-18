class Solution:
    def possible(self, index, current, ans, digits):
        cnt = ["","","abc","def","ghi","jkl","mno","pqrs","tuv","wxyz"]
        if index == len(digits):
            ans.append(current)
            return
            
        s = cnt[int(digits[index])]
        for i in s:
            self.possible(index + 1, current + i, ans, digits)
            
    def letterCombinations(self, digits):
        ans = []
        if not digits:
            return ans
        self.possible(0, "", ans, digits)
        return ans