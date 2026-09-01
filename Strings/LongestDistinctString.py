''' 
Longest Substring With At Most K Distinct Characters:
Given a string s and an integer k.Find the length of the longest substring with at most k distinct characters.
'''

class Solution:
    def kdistinctchar(self, s, k):
        l, r = 0, 0
        n = len(s)
        mpp = {}
        max_len = 0
        while r < n:
            if s[r] in mpp:
                mpp[s[r]] += 1
            else:
                mpp[s[r]] = 1
            if len(mpp) > k:
                mpp[s[l]] -= 1
                if mpp[s[l]] == 0:
                    del mpp[s[l]]
                l += 1
            max_len = max(max_len, r - l + 1)
        return max_len