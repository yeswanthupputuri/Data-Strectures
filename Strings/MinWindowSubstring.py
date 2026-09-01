class Solution:
    def minWindow(self, s, t):
        mpp =[0] * 256
        for i in t:
            mpp[ord(i)] += 1
        min_len = float('inf')
        sind = -1
        l, r = 0, 0
        cnt = 0
        while r < n:
            if mpp[ord(s[r])] > 0:
                cnt += 1
            mpp[ord(s[r])] -= 1
            while cnt == len(t):
                if r - l + 1 < min_len:
                    min_len = r - l + 1
                    sin = l
                mpp[ord(s[l])] += 1
                if mpp[ord(s[l])] > 0:
                    cnt -= 1
                l += 1
            r += 1
        return s[sind:sind+min_len] if sind != -1 else ""