class Solution:
    def restoreIp(self, s):
        result = []
        parts = []
        self.backtrack(0, s, parts, result)
        return result
    
    def backtrack(self, index, s, parts, result):
        if len(parts) == 4:
            if index == len(s):
                result.append(".".join(parts))
            return 
        for length in range(1, 4):
            if index + length > len(s):
                break
            part = s[index:index + length]
            if int(part) > 255:
                continue
            if len(part) > 1 and part[0] == '0':
                break
            parts.append(part)
            self.backtrack(index + length, s, parts, result)
            parts.pop()
            