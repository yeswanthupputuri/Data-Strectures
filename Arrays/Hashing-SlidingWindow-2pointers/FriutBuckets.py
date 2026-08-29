class Solution:
    def totalfruites(self, fruits):
        n = len(fruits)
        max_len = 0
        mpp = {}
        l, r = 0, 0
        while r < n:
            mpp[fruits[r]] = mpp.get(fruits[r], 0) + 1
            if len(mpp) > 2:
                mpp[fruits[l]] -= 1
                if mpp[fruits[l]] == 0:
                    del mpp[fruits[l]]
                l += 1
            if len(mpp) <= 2:
                max_len = max(max_len, r - l + 1)
            r += 1
        return max_len