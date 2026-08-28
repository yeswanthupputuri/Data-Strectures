''' 
Given an integer array nums. Find the subarray with the largest product, and return the product of the elements present in that subarray.
A subarray is a contiguous non-empty sequence of elements within an array.

Example 1
Input: nums = [4, 5, 3, 7, 1, 2]
Output: 840
'''

class Solution:
    def maxProdArray(self, nums):
        n = len(nums)
        result = float('-inf')
        prefix = 1
        suffix = 1
        for i in range(n):
            if prefix == 0:
                prefix = 1
            if suffix == 0:
                suffix = 1
            prefix = prefix * nums[i]
            suffix = suffix * nums[n - i - 1]
            result = max(result, max(prefix, suffix))
        return result