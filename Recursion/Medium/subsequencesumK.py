""" 
Given an array nums and an integer k. R﻿eturn true if there exist subsequences such that 
the sum of all elements in subsequences is equal to k else false.

Example 1

Input : nums = [1, 2, 3, 4, 5] , k = 8
Output : Yes

"""
class Solution:
    def possible(self, index, target, nums):
        if target < 0:
            return False 
        if target == 0:
            return True 
        if index == len(nums):
            return target == 0
        
        if self.possible(index + 1, target - nums[index], nums):
            return True 
        if self.possible(index + 1, target, nums):
            return True 
        return False
        
    def checksubsequence(self, nums, target):
        n = len(nums)
        return self.possible(0, target, nums)
    
"""  
Given an array nums and an integer k.Return the number of non-empty subsequences of nums 
such that the sum of all elements in the subsequence is equal to k.

Example 1
Input : nums = [4, 9, 2, 5, 1] , k = 10
Output : 2
Explanation : The possible subsets with sum k are [9, 1] , [4, 5, 1].

class Solution:
    def func(self, ind, sum, nums):
        if sum == 0:
            return 1
        if sum < 0 or ind == len(nums):
            return 0
        return self.func(ind + 1, sum - nums[ind], nums) + self.func(ind + 1, sum, nums)

    def countSubsequenceWithTargetSum(self, nums, target):
        return self.func(0, target, nums)


"""
        