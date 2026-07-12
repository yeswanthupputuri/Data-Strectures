""" 
Given an array nums of n integers. Return array of sum of all subsets of the array nums.
Output can be returned in any order.

Example 1:
Input : nums = [2, 3]
Output : [0, 2, 3, 5]

"""
class Solution:
    def possible(self, index, sum, nums, result):
        if index == len(nums):
            result.append(sum)
            return
        self.possible(index + 1, sum + nums[index], nums, result)
        self.possible(index + 1, sum , nums, result)
        
    def subset(self, nums):
        n = len(nums)
        result = []
        self.possible(0, 0, nums, result)