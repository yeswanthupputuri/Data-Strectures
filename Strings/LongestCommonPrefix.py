class Solution:
    def longestCommonprefix(self, st):
        if not st:
            return ""
        st.sort()
        s1 = st[0]
        s2 = st[1]
        maxi = ""
        for i in range(min(len(s1), len(s2))):
            if s1[i] == s2[i]:
                maxi += s1[i]
            else:
                break
        return maxi
    #Time Complexity : O(N * M * logN)
    
# Horizantel Scanning 
# strs = ["flowers", "flow", "fly", "flight"]
class Solution:
    def longestCommonPrefix(self, st):
        if not st:
            return ""
        prefix = st[0]
        for i in range(1, len(st)):
            while not st[i].startswith(prefix):
                prefix = prefix[:-1]
                if prefix == "":
                    return ""
        return prefix
    
class solution:
    def sortbyfre(self, s):
        mpp = {}
        for ch in s:
            if ch not in mpp:
                mpp[ch] = 0
            mpp[ch] += 1
        result = sorted(mpp, key=lambda ch: (-mpp[ch], ch))
        return result
            
            
        