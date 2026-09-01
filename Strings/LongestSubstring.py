'''
Longest Substring Without Repeating Characters :

Given a string, S. Find the length of the longest substring without repeating characters.
'''
class Solution:
    def longestsubstring(self, s):
        mpp = [-1] * 256
        l, r = 0, 0
        max_len = 0
        n = len(s)
        while r < n:
            if mpp[ord(s[r])] != -1:
                l = max(mpp[ord(s[r])] + 1, l)
            curr_len = r - l + 1
            max_len = max(max_len, curr_len)
            mpp[ord(s[r])] = r
            r += 1
        return max_len