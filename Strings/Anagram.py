class Solution:
    def anagrame(self, s, t):
        if len(s) != len(t):
            return False 
        cnt = [0] * 26
        for i in t:
            cnt[ord(i) - ord('a')] += 1
        for i in s:
            cnt[ord(i) - ord('a')] -= 1
        for i in cnt:
            if i != 0:
                return False 
        return True