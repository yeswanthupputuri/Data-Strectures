''' 
Max Consecutive Ones III :

Given a binary array nums and an integer k, flip at most k 0's.
Return the maximum number of consecutive 1's after performing the flipping operation.

Example 1
Input : nums = [1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0] , k = 3
Output : 10
'''

class Solution:
    def longestones(self, nums, k):
        l, r = 0, 0
        n = len(nums)
        zeros = 0
        max_len = 0
        while r < n:
            if nums[r] == 0:
                zeros += 1
            if zeros > k:
                if nums[l] == 0:
                    zeros -= 1
                l += 1
            if zeros <= k:
                max_len = max(max_len, r - l + 1)
            r += 1
        return max_len
                
            