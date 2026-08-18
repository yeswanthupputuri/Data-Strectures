class Solution:
    def pali(self,start,end,s):
        while start <= end:
            if s[start] != s[end]:
                return False 
            start += 1
            end -= 1
        return True

    def poss(self, ind, s, ans,curr):
        if ind == len(s):
            ans.append(curr[:])
            return 
        for i in range(ind, len(s)):
            if self.pali(ind, i, s):
                curr.append(s[ind:i+1])
                self.poss(i + 1, s, ans, curr)
                curr.pop()
                
    def partition(self, s: str):
        ans = []
        curr = []
        self.poss(0,s,ans,curr)
        return ans
