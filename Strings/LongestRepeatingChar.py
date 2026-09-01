'''  
Longest Repeating Character Replacement :

Given an integer k and a string s, any character in the string can be selected and changed to any other uppercase English character. 
This operation can be performed up to k times. After completing these steps, return the length of the longest substring that contains the same letter.
'''

class Solution:
    def characterreplacement(self, s, k):
        n = len(s)
        l, r = 0, 0
        max_len = 0
        maxfre = 0
        mpp = [0] * 256
        while r < n:
            mpp[ord(s[r]) - ord('A')] += 1
            maxfre = max(maxfre, mpp[ord(s[r]) - ord('A')])
            if (r - l + 1) - maxfre > k:
                mpp[ord(s[l]) - ord('A')] -= 1
                l += 1
            max_len = max(max_len, r - l + 1)
            r += 1
        return max_len