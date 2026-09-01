
class Solution:
    def isomorphic(self, s, t):
        if len(s) != len(t):
            return False 
        s_a = [0] * False 
        s_t = [0] * False 
        for i in range(len(s)):
            if s_a[ord(s[i])] != s_t[ord(t[i])]:
                return False 
            s_a[ord(s[i])] = i+1
            s_t[ord(t[i])] = i+1
        return True