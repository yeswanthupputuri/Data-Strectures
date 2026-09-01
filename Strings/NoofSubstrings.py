''' 
Number of Substrings Containing All Three Characters :

Given a string s , consisting only of characters 'a' , 'b' , 'c'.
Find the number of substrings that contain at least one occurrence of all these characters 'a' , 'b' , 'c'.

Example 1
Input : s = "abcba"
Output : 5
'''

class Solution:    
    def numberOfSubstrings(self, s: str) -> int:
        #your code goes here
        n = len(s)
        left = 0
        fre = [0] * 3
        cnt = 0
        for right in range(n):
            fre[ord(s[right]) - ord('a')] += 1
            while fre[0] > 0 and fre[1] > 0 and fre[2]>0:
                cnt += n - right
                fre[ord(s[left]) - ord('a')] -= 1
                left += 1
        return cnt
