"""
Given string str containing just the characters '(', ')', '{', '}', '[' and ']' .
check if the input string is valid and return true if the string is balanced otherwise return false.

Example 1

Input: str = “()[{}()]”
Output: True

"""

class Solution:
    def checkmatch(self, open, close):
        if open == "(" and close == ")":
            return True
        if open == "{" and close == "}":
            return True
        if open == "[" and close == "]":
            return True
        return False
    
    def balencedparanthesis(self, s):
        st = []
        for i in range(len(s)):
            if s[i] == "(" or s[i] == "{" or s[i] == "[":
                st.append(s[i])
            else:
                if not st:
                    return False
                ch = st[-1]
                st.pop()
                if not self.checkmatch(ch, s[i]):
                    return False
        return not st
                    